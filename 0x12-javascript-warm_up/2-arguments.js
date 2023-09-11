#!/usr/bin/node
// This script prints a message depending of the number of arguments passed

const length = process.argv.length - 2;

if (!length) {
  console.log('No argument');
} else if (length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
