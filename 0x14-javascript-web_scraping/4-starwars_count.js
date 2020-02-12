#!/usr/bin/node
const request = require('request');
let dict = {};
let count = 0;
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    dict = JSON.parse(body);
    for (let i = 0; i < dict.results.length; i++) {
      for (let j = 0; j < dict.results[i].characters.length; j++) {
        if (dict.results[i].characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
