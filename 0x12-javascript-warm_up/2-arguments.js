#!/usr/bin/node
{
  const argu = (process.argv.length - 2);
  if (argu === 0) {
    console.log('No argument');
  } else if (argu === 1) {
    console.log('Argument found');
  } else if (argu > 1) {
    console.log('Arguments found');
  }
}
