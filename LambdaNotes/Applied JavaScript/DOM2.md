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