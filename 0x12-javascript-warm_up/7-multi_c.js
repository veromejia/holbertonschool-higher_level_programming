#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < arg) {
    console.log('C is fun');
    i++;
  }
}
