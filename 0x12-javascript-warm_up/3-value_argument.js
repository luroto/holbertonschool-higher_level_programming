#!/usr/bin/node
let counter = 0;
process.argv.forEach((val, index) => {
  counter++;
});
if (counter > 2) {
  console.log(process.argv[2]);
}
if (counter <= 2) {
  console.log('No argument');
}
