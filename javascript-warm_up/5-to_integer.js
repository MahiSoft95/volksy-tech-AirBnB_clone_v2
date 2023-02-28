#!/usr/bin/node

const cm = Number(process.argv.slice(2));
if (isNaN(cm)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + cm);
}
