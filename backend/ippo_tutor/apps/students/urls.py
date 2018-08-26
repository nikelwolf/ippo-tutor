from rest_framework import routers

from .views import StudentProfileViewSet

router = routers.DefaultRouter()
router.register('', StudentProfileViewSet)

urlpatterns = [

]

urlpatterns += router.urls

