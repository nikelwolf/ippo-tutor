from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from ippo_tutor.apps.core.permissions import IsTutorOrTargetUser, IsTutor

from .models import StudentProfile
from .serializers import StudentProfileSerializer


class StudentProfileViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = StudentProfile.objects.select_related('user')
    serializer_class = StudentProfileSerializer
    lookup_field = 'username'

    def get_object(self):
        username = self.kwargs['username']
        user = generics.get_object_or_404(self.queryset, user__username=username)
        self.check_object_permissions(self.request, user)
        return user

    def get_permissions(self):
        permission_classes = self.permission_classes[:]
        if self.action in ['list', 'update']:
            permission_classes += [IsTutor]
        else:
            permission_classes += [IsTutorOrTargetUser]

        return [permission() for permission in permission_classes]
