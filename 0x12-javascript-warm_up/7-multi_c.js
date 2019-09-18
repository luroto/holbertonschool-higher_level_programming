#!/usr/bin/node
const printing = 'C is fun';
let conta = 0;
const occur = parseInt(process.argv[2]);
if (isNaN(occur) === true) {
  console.log('Missing number of occurrences');
} for (conta = 0; conta < occur; conta++) {
  console.log(printing);
}
