# Chapter 10 Modules

> Write code that is easy to delete, not easy to extend.

## Modules
`Modules` are an attempt to avoid big bundles of unorganized code. 

A module is a piece of a program that specifies which other pieces it relies on and which functionality it provides for other modules to use (it's interface).

The relations between modules are called `dependencies`. When a module needs a piece from another module, it is said to depend on that module. When this fact is clearly specified in the module itself, it can be used to figure out which other modules need to be present to be able to use a given module and to automatically load dependencies.

## Packages

One of the advantages of building a program out of separate pices, and being actually able to run those pieces on their own, is that you might be able to apply the same piece in different programs.

Once you start duplicating code, you'll quickly find yourself wasting time and energy moving copies around and keeping them up to date.

> That is where `packages` come in.

A package is a chunk of code that can be distributed. It may contain one or more modules and has information about which other packages it depends on.

### NPM

NPM is two things: an online service where one can download packages, and a program that helps you install and manage those packages.

## CommonJS

The most widely used approach to bolted-on JS modules is called `CommonJS Modules`.

The main concept in CommonJS modules is a function called `require`.

    const ordinal = require('ordinal')
    const {days, months} = require('date-names')

    exports.formatDate = function(date, format) {
      return format.replace(/YYYY|M(MMM)?Do?|dddd/g, tag => {
        if (tag == "YYYY") return date.getFullYear();
        if (tag == "M") return date.getMonth();
        if (tag == "MMMM") return months[date.getMonth()];
        if (tag == "D") return date.getDate();
        if (tag == "Do") return ordinal(date.getDate());
        if (tag == "dddd") return days[date.getDay()];
      })
    }

  > We can define `require` in its most minimal form like so:

    require.cache = Object.create(null)

    function require(name) {
      if(!(name in require.cache)) {
        let code = readFile(name)
        let module = {exports: {}}
        require.cache[name] = module
        let wrapper = Function("require, exports, module", code)
        wrapper(require, module.exports, module)
      }

      return require.cache[name].exports
    }

## ECMAScript Modules

The main concepts of dependencies and interfaces remain the same but the details differ. For one thing the notation is now integrated into the language. Instead of calling a funtion to access a dependency you use a special `import` keyword

Another important difference is that ES module imports happen before a modules script starts running. That means import declarations may not appear inside funtions or blocks, and the names of dependencies must be quoted strings, not arbitrary expressions.