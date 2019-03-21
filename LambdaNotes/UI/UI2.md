---The Box Model
    A pattern for positioning HTML elements on the page using CSS

    Box model is one of the most important skills in front end development
    As style start to get added, the items start to get bigger.

    Margin is the outermost element in the box model
    then comes the Border
    after the border is the padding
    and after the padding is the content itself

    Content- space within the model in which our text and images are rendered
    Padding- the spacing between the content and border
    Border- a border that we can style around the padding
    Margin- the space between the border and the rest of the page.

---CSS Display Properties
    Box-model does present a few limitations

    CSS display property allows us to overcome some of the short comings of box model.

    display: none; - removes the html element from the page's flow
        used when temporarily hiding content.
        can be toggled with JavaScript
        REMOVES THE ELEMENT FROM THE DOCUMENT

    display: inline; - allows for elements to be nested within other elements without
        disrupting the flow of content
        a && span both are examples of inline elements
        height, width have no effect
        only takes up as much space as it's content.
        BLOCK are not to be nested within inline elements
        can use vertical-align to position elements vertically. -- not avail with block
        can ust text-align to position elements horizontally. -- not avail with block

    display: block; - divs are block level elements
        block elements take up as much space as their parent element
        if you want to control block elements you will need to employ bnoth the height, width properties
        You can nest block and inline elements within block elements
        all block elements will start on a new line
        Takes up as much height and width as the parent element allows
        Use margin: auto to center horizontally.
        difficult to vertically center

    display: inline-block;
        sometimes we dont want block elements abrupt behavior in our layouts but we want the control it can provide with height, and width
        Will have default behavior of inline elements with the added bonus of controlling the size.
        Inline behavior allows elements to stack next to each other

---CSS Reset