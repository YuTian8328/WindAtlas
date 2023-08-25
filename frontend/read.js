const fs = require('fs');
const jpickle = require('jpickle');
const binary = fs.readFileSync('test.dat');
const data = jpickle.loads(binary)
console.log(data)