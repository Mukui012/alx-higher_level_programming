#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  for (const k in list) {
    if (list[k] === searchElement) {
      total++;
    }
  }
  return total;
};
