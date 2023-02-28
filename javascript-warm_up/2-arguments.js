#!/usr/bin/node

const cm = process.argv
if (cm.length<3){
  console.log('No argument')
}else if (cm.length == 3){
  console.log('Argument found')
}else{
  console.log('Arguments found')
}

