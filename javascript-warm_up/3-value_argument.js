#!/usr/bin/node

const cm = process.argv;
if (cm[2]) {
  console.log(cm[2]);
} else {
  console.log('No argument');
}
