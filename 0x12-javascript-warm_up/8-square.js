#!/usr/bin/node
const size = parseInt(process.argv[2]);
let i;
if (isNaN(size) === true) {
  console.log('Missing size');
}
for (i = 0; i < size; i++) {
  console.log('X'.repeat(size));
}
