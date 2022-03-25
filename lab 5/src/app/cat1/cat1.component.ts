import { Component, OnInit } from '@angular/core';
import { firstcat } from '../firstcat';

@Component({
  selector: 'app-cat1',
  templateUrl: './cat1.component.html',
  styleUrls: ['./cat1.component.css']
})

export class Cat1Component implements OnInit {
  firstcat = firstcat;

  constructor() { }

  ngOnInit(): void {
  }

  onRemove(cat1: any){
    const index = this.firstcat.indexOf(cat1);
    this.firstcat.splice(index, 1);
  }

}
