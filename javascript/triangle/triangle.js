"use strict";

class Triangle {
  constructor(a, b, c) {
    this.allSides = [a, b, c].sort(( a, b ) => a - b );
  }

  kind(){
    var a = this.allSides[0];
    var b = this.allSides[1];
    var c = this.allSides[2];

    if(a * b * c == 0) throw "Must have a side";
    if(a < 0 || b < 0 || c < 0) throw "Must have positive sides";
    if(a + b <= c) throw "Must pass triangle inequality";

    if(a == b && b == c) return "equilateral";
    if( a == b || a == c || b == c) return "isosceles";
    return "scalene";
  }
}

module.exports = Triangle;
