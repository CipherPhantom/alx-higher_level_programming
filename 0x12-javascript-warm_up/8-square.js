#!/usr/bin/node
// This script prints a square

const size = parseInt(process.argv[2]);

if (size) {
  for (let i = 0; i < size; i++) {
    let width = '';

    for (let i = 0; i < size; i++) {
      width += 'X';
    }
    console.log(width);
  }
} else {
  console.log('Missing size');
}
