#!/usr/bin/node
{
  let counter;
  process.argv.forEach((val, index) => {
    counter = index;
  });
  if (counter > 1) {
    console.log(process.argv[2]);
  }
  if (counter === 1) {
    console.log('No argument');
  }
}
