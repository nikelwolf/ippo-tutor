//dead todo

import {
    Directive,
    Input,
    OnInit,
    TemplateRef,
    ViewContainerRef
  } from '@angular/core';
  
  import { UserService } from '../core';
  
  @Directive({ selector: '[appShowAuthed]' })
  export class ShowAuthedDirective implements OnInit {
    constructor(
      private templateRef: TemplateRef<any>,
      private userService: UserService,
      private viewContainer: ViewContainerRef
    ) {}
  
    condition: boolean;
    isAuthenticated: boolean;
  
    ngOnInit() {
      this.userService.isAuthenticated.subscribe(
        (isAuthenticated) => {
          this.isAuthenticated = isAuthenticated; 
        }
      );
    }
  
    @Input() set appShowAuthed(condition: boolean) {
      this.condition = condition;
      if (this.isAuthenticated && this.condition || !this.isAuthenticated && !this.condition) {
        this.viewContainer.createEmbeddedView(this.templateRef);
      } else {
        this.viewContainer.clear();
      }
    }
  
  }