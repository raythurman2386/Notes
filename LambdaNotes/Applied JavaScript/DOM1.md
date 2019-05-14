#DOM

  The Document Object Model is an object representation of the html elements of a webpage.

  The Object Model is a tree structure with each DOM element, therefore being a tree node, containing all the same property keys as each other node.

  When the DOM is built and the webpage is loaded, we gain access to it in the form of the global JS object 'document'

  Document contains dozens of built in methods and properties

#DOM Selectors
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


#Manipulate Data in the DOM
  after we have saved our element to a variable, we can then use that instance of the element to access and assign values.
  Here are the most commonly used methods:

    .textContent
      gets and sets the text of an element
      uses the assignment operator to reset the text
      element.textContent = 'Something New';

    .setAttribute();
      used as a way to set or reassign an attribute on the element
      takes two arguments, the attribute to set, and the value to set it to
      element.setAttribute('src', 'http://www.imagsource.com/image.jpg'); --or--
      element.src = 'http://www.imagsource.com/image.jpg';

    .style
      can be used to add inline styles to an object
      uses the assignment operator to change the styling
      This DOES NOT change anything in the CSS file
      element.style.color = 'blue';

    .className, .id
      className accesses or assigns a string containing all of the classes on the element
      id accesses or assigns a string containing the id of the element

    .classList
      classList will return an array-like object of all the classes on the element. There are a number of useful methods available on classList
        classList is a DOMTokenList
          a DOMTokenList is an array-like object with a numerical zero-based index, a length property,
          also .contains() and .forEach() methods
        Most notable the methods .add() .remove() and .toggle() exist
          .add('className') and .remove('.className') do as their name indicates
          .toggle('className') will add the class if it does not exist and remove it if it does

    .appendChild() and .prepend()
      these are used to add child elements to parent elements
      .append will add and item to the end of the parent elements
        parentElement.appendChild(childElement);
      .prepend add the child to the beginning, which will cause it to display first
        parentElement.prepend(childElement);

    .children and .parentNode
      used for accessing relatives of the element
      .children returns a HTMLCollection of all the children of that element
      .parentNode returns the parent element of that element
    
#Create a new Element and add it to the DOM
    
    document.createElement('h1');
  creates a new element
  element will exist in memory but not quite in the dom yet

  .append and .prepend will add these newly created elements to the DOM