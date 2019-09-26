#!/usr/bin/node
exports.esrever = function (list) {
  const len = (list.length) - 1;
  const newlist = [];
  for (let i = len; i >= 0; i--) {
    newlist.push(list[i]);
  }
  return (newlist);
};
