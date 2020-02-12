#!/usr/bin/node
const request = require('request');
const myFile = require('fs');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    myFile.writeFile(process.argv[3], body, 'utf-8', function (error, data) {
      if (error) {
        console.log(error);
      }
    });
  }
});
