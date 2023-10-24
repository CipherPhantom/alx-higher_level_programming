#!/usr/bin/node
// This script prints the title of a Star Wars movie
// where the episode number matches a given integer

const request = require('request');

const id = process.argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${id}`,
  (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const data = JSON.parse(body);
      console.log(data.title);
    }
  });
