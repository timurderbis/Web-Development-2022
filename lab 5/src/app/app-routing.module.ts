import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CommonModule } from '@angular/common';
import {ProductListComponent} from './product-list/product-list.component';
import {ProductDetailsComponent} from './product-details/product-details.component';
import {CategoryComponent} from './category/category.component';
import {Cat1Component} from './cat1/cat1.component';
import {Cat2Component} from './cat2/cat2.component';
import {Cat3Component} from './cat3/cat3.component';
import {Cat4Component} from './cat4/cat4.component';

const routes: Routes = [
  {path: '', component: CategoryComponent},
  {path: 'category', component: CategoryComponent},
  {path: 'productdetails', component: ProductDetailsComponent},
  {path: 'firstcat', component: Cat1Component},
  {path: 'secondcat', component: Cat2Component},
  {path: 'thirdcat', component: Cat3Component},
  {path: 'fourthcat', component: Cat4Component}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
