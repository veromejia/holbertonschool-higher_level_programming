#!/usr/bin/node
const x = process.argv[2];
if (isNaN(x) || x === undefined) {
  console.log('Not a number');
} else {
  console.log('My number: ' + x);
}
