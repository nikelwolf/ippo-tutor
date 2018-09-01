import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { LoginFormComponent } from './login-form/login-form.component';
import { UploadFormComponent } from './upload-form/upload-form.component';
import {RouterModule} from '@angular/router';

const routes = [
  {path: 'upload', component: UploadFormComponent},
  {path: 'login', component: LoginFormComponent},
];

// @ts-ignore
@NgModule({
  declarations: [
    AppComponent,
    LoginFormComponent,
    UploadFormComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }