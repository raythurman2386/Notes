// for (var i = 0; i < 3; i++) {
//   setTimeout(function () { alert(i); }, 1000 + i);
// }

;(function() {
  var a = (b = 5)
})()

console.log(b)

// CamelCase
function camalize(str) {
  return str
    .toLowerCase()
    .replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => chr.toUpperCase())
}

console.log(camalize('How *are -You _doing'))
