#!/usr/bin/node
function add(a, b){
    console.log(a+b);
}

a = parseInt(process.argv[2]);
b = parseInt(process.argv[3]);
add(a, b);
