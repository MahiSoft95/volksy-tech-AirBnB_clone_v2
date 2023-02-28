#!/usr/bin/node

const text = 'C is fun';
const num = Number(process.argv.slice(2));
if (isNaN(num)) {
  console.log('Missing number of occurrences');
else {
 let i = 0;
for (let i = 0; i < num;  i++) {
		console.log(text);
}
  }
