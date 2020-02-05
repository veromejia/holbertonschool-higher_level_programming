#!/usr/bin/node
const args = process.argv.slice(2);
if (process.argv.length <= 3) {
  console.log('0');
} else {
  args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
