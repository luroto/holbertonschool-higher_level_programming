#!/usr/bin/node
const num = parseInt(process.argv[2])
if (isNaN(num) === true) {
  console.log('Not a number');
} else if (typeof(num) === 'number') {
  console.log(`My number is ${num}`);
}
