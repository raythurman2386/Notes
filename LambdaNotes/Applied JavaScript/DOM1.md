DOM

  The Document Object Model is an object representation of the html elements of a webpage.

  The Object Model is a tree structure with each DOM element, therefore being a tree node, containing all the same property keys as each other node.

  When the DOM is built and the webpage is loaded, we gain access to it in the form of the global JS object 'document'

  Document contains dozens of built in methods and properties

DOM Selectors
  DOM selectors are case sensitive.
  These are all of the older selectors

    document.getElementByTagName('p');

    document.getElementById('idName');

    document.getElementByClassName('className');
  
  Other than id these will return an array of the items you are trying to select.

  Here are some of the newer selectors
  We can select by element, id, class or others with both methods

    document.querySelector('.custom-style');
      This method will search for and return the first element that matches the value passed into the method.

    document.querySelectorAll('queryString');
      This method will search for and return all elements matching the query string and will return them as 
      an array like object called a NodeList.

Difference between HTMLCollection, NodeList, and Array
  They both have numerical zero-baed indices, and the length property but that is all they share with an array. 
  NodeList does take it one step further and has access to .forEach. There is no .reduce or .map though.

  the array class does contain a method we can use to create an array from an array-like object, called .from();
  to use this we would simply give .from the array-like object as it's only arg

    Array.from(arrayLikeObject);


    