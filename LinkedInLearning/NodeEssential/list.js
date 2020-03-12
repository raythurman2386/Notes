const fs = require('fs')

console.log("Started reading files")

fs.readdir('./assets', (err, files) => {
  if(err) {
    throw err;
  }

  console.log("complete")
  console.log(files)
})

// Readfile
fs.readFile('./assets/Readme.md', 'UTF-8', (err, text) => {
  if(err) {
    throw err;
  }

  console.log(text)
})

fs.readFile('./assets/alex.jpg', 'UTF-8', (err, img) => {
  if (err) {
    throw err;
  }

  console.log(img)
})