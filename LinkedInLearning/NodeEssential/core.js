const path = require('path')
const util = require('util')
const v8 = require('v8')

util.log(path.basename(__filename))

util.log(v8.getHeapStatistics())

// Readline module
const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

rl.questions("How do you like Node?", answer => {
  console.log(`Your answer: ${answer}`)
})