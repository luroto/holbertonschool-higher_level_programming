#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
let c = 0;
function add (a, b) {
  c = a + b;
  console.log(c);
}
add(a, b);
