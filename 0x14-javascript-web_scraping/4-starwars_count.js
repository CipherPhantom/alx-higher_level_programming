#!/usr/bin/node
// This script prints the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');

request(process.argv[2],
  (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const data = JSON.parse(body);
      const films = data.results;
      let count = 0;

      for (const film of films) {
        if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          count++;
        }
      }
      console.log(count);
    }
  });
