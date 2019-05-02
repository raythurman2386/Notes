Event Listeners

Every interaction a user has with a site is known as an event, a click, moving the mouse, scrolling 
the page, pressing a key on the keyboard.

MDN lists every event we can access

  .addEventListener

    element.addEventListener('click', callback);

  The callback is also known as the event handler, will take a single argument, known as the 'event object'

  This is a JS Object and contains all we need to know about the event and the element that it was triggered on.

    element.addEventListener('click', (event) => {//Handle event});

Event Propagation

  Event propagation can cause headaches when dealing with events. It is best to learn how to recognize this fewture and how to properly prevent it from happening

  If you trigger an event on a child element, you are also triggering that same event on every parent element all the way up to the body.

  This process is called event propagation.

  In our event handler, we are passed the event object. 

  The event object has a method called .stopPropagation().

  if we call this method in our event handler, on our event, it will effectively stop our event from bubbling any further up the chain.

    const eventHandler = e => { e.stopPropagation() }

Prevent Default

  some elements have a native default reactin to certain events.
  
  .preventDefault is a method on the event object and it will stop an HTML element from reacting in its default way.