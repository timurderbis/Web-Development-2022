import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductDetailsComponent } from './product-details/product-details.component';
import { AppRoutingModule } from './app-routing.module';
import { CategoryComponent } from './category/category.component';
import { Cat1Component } from './cat1/cat1.component';
import { Cat2Component } from './cat2/cat2.component';
import { Cat3Component } from './cat3/cat3.component';
import { Cat4Component } from './cat4/cat4.component';
import { LikeComponent } from './like/like.component';

@NgModule({
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      { path: '', component: ProductListComponent },
    ]),
    AppRoutingModule
  ],
  declarations: [
    AppComponent,
    TopBarComponent,
    ProductListComponent,
    ProductDetailsComponent,
    CategoryComponent,
    Cat1Component,
    Cat2Component,
    Cat3Component,
    Cat4Component,
    LikeComponent,
  ],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }


