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

// Writefile
const md = `
# This is a new file

We can write text to a file with fs.writefile

* fs.readdir
* fs.readFile
* fs.writeFile
`

fs.writeFile('./assets/note.md', md.trim(), (err) => {
  if(err) {
    throw err
  }

  console.log('File saved')
})

fs.mkdir("storage-files", err => {
  if(err) {
    throw err
  }

  console.log("Directory Created")
})

// Append Files
const colorData = require('./assets/colors.json')

colorData.colorList.forEach(
  color => {
    fs.appendFile('./storage-files/colors.md', `${color.color}: ${color.hex} \n`, 
    err => {
      if(err) {
        throw err
      }
    })
})

// Rename
fs.renameSync("./assets/colors.json", './assets/colorData.json')
fs.rename("./assets/notes.md", "./storage-files/notes.md", err => {
  if(err) {
    throw err
  }
})

setTimeout(() => {
  fs.unlinkSync("./assets/alex.jpg")
}, 4000)

// Removes all files from directory to be removed
fs.readdirSync("./storage-files").forEach(fileName => {
  fs.unlinkSync(`./storage-files/${fileName}`)
})

fs.rmdir('./storage-files', err => {
  if (err) {
    throw err
  }

  console.log('Directory removed')
})