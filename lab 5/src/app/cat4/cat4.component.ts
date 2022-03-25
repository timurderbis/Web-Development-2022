import { Component, OnInit } from '@angular/core';
import { fourthcat } from '../fourthcat';

@Component({
  selector: 'app-cat4',
  templateUrl: './cat4.component.html',
  styleUrls: ['./cat4.component.css']
})
export class Cat4Component implements OnInit {
  fourthcat = fourthcat;
  constructor() { }

  ngOnInit(): void {
  }
  onRemove(cat1: any){
    const index = this.fourthcat.indexOf(cat1);
    this.fourthcat.splice(index, 1);
  }

}
