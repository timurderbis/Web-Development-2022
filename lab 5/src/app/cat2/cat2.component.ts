import { Component, OnInit } from '@angular/core';
import {secondcat } from '../secondcat';

@Component({
  selector: 'app-cat2',
  templateUrl: './cat2.component.html',
  styleUrls: ['./cat2.component.css']
})
export class Cat2Component implements OnInit {
  secondcat = secondcat;
  constructor() { }

  ngOnInit(): void {
  }

  onRemove(cat1: any){
    const index = this.secondcat.indexOf(cat1);
    this.secondcat.splice(index, 1);
  }

}
