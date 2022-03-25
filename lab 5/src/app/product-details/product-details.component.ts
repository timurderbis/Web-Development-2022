import { Component } from '@angular/core';
import { category } from '../category';
import {products} from '../products';

@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.css']
})
export class ProductDetailsComponent{
  category = category;
  products = products;

  constructor() { }

}
