#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c !== 'undefined') {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
