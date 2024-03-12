#!/usr/bin/node
const dict = require('./101-data.js').dict;
let newDict = {};

for (let key in dict) {
  const value = dict[key];

  if (typeof value === 'number') {
    if (newDict[value] === undefined) {
      newDict[value] = [key];
    } else {
      newDict[value].push(key);
    }
  } else {
    console.warn(`Skipping non-numeric value (${value}) for key ${key}.`);
  }
}

const sortedKeys = Object.keys(newDict).sort((a, b) => a - b);
sortedKeys.forEach(key => {
  console.log(`${key}: [${newDict[key].join(', ')}]`);
});
