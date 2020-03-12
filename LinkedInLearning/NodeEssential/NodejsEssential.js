const path = require('path')

// console.log(__dirname)
// console.log(__filename)

console.log(`The file name is ${path.basename(__filename)}`)

// Global Process object
console.log(process.pid)
console.log(process.versions.node)

// Argument Processes typeOf Array
console.log(process.argv)

function grab(flag) {
  let indexAfterFlag = process.argv.indexOf(flag) + 1
  return process.argv[indexAfterFlag]
}

const greeting = grab("--greeting")
const user = grab("--user")

console.log(`${greeting} ${user}`)