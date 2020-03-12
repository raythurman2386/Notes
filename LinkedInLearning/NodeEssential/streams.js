const fs = require('fs')

const readStream = fs.createReadStream('./assets/lorum-ipsum.md', 'UTF-8')

let fileText = ""

console.log('type something...')

readStream.on("data", data => {
  console.log(`I read ${data.length -1} characters of text`)
  fileText += data
})

readStream.once("data", data => {
  console.log(data)
})

readStream.on("end", () => {
  console.log("The stream has ended")
  console.log(`In total I read ${fileText.length - 1} characters of text`)
})

// writeable stream
const writeStream = fs.createWriteStream('./assets/myFile.txt', 'UTF-8')

writeStream.write("hello")
writeStream.write("world \n")

readStream.on('data', (data) => {
  writeStream.write(data)
})

readStream.pipe(writeStream)