#!/usr/bin/node

const Error = 'Missing number of occurrences';

const arg = Math.floor(+process.argv[2]);

if (isNaN(arg)) {
  console.log(Error);
} else {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
}
