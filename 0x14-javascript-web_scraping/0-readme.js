#!/usr/bin/node
// This script reads and prints the content of a file.

const fs = require('fs');

fs.readFile(process.argv[2],
  'utf-8',
  (error, data) => {
    if (error) {
      console.log(error);
    } else {
      console.log(data);
    }
  });
