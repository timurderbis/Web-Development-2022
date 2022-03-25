import { Component, OnInit } from '@angular/core';
import {thirdcat } from '../thirdcat';

@Component({
  selector: 'app-cat3',
  templateUrl: './cat3.component.html',
  styleUrls: ['./cat3.component.css']
})
export class Cat3Component implements OnInit {
  thirdcat = thirdcat;
  constructor() { }

  ngOnInit(): void {
  }
  onRemove(cat1: any){
    const index = this.thirdcat.indexOf(cat1);
    this.thirdcat.splice(index, 1);
  }

}
