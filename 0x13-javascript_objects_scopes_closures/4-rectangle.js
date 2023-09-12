#!/usr/bin/node
/*
*class Rectangle that defines a rectangle
*use class notation for defining your class
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let n = 0; n < this.height; n++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const k = this.width;
    this.width = this.height;
    this.height = k;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
