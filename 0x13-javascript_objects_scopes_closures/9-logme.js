#!/usr/bin/node

let counter = 0;
exports.logMe = function (item) {
  function printLog (item) {
    console.log(`${counter}: ${item}`);
    counter++;
  }
  return printLog(item);
};
