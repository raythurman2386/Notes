const path = require('path')

// console.log(__dirname)
// console.log(__filename)

console.log(`The file name is ${path.basename(__filename)}`)

// Global Process object
console.log(process.pid)
console.log(process.versions.node)