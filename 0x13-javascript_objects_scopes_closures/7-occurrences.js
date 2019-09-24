#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocur = 0;
  let item;
  for (item of list) {
    if (item === searchElement) {
      ocur++;
    }
  }
  return ocur;
};
