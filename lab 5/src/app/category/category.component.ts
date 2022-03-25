import { Component, OnInit } from '@angular/core';
import { category } from '../category';
import { products} from '../products';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {
  category = category;
  products = products;

  constructor() { }

  ngOnInit(): void {
  }

}
