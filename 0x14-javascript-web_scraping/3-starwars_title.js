#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, 'utf8', function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
