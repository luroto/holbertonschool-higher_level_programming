#!/usr/bin/node

const SquareB = require('./5-square');
const Square = class Square extends SquareB {
  charPrint (c) {
    if (typeof c !== 'undefined') {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    } else {
      super.print();
    }
  }
};
module.exports = Square;
