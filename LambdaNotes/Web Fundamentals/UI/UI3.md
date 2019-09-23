--- FLEXBOX
Flex box only works on block level elements and can be nested.
But flex box will only go one level deep

Flex box is a module of CSS

display: flex; invokes a whole module of options to use.

The flex box module was designed to only nest one level deep

flex-direction default is row.
    row
    row-reverse
    column
    column-reverse

Container rules and Properties
    Flex applies styles to the parent container and children start behaving differently

    Whichever element gets display: flex becomes the flex container.
    all nested elements become the flex-items.

    flex-direction, flex-wrap, flex-flow, justify-content, align-content, align-items

Flex-direction
    all flex modules follow a general direction
    default direction is row
    this direction is the main axis

    -Main axis will flow from left to right
        row-reverse will make axis flow from right to left
        column will flow from top to bottom
        column-reverse will flow from bottom to top

Flex-wrap
    flex items will often run over content within a containers space
    when this happens use flex-wrap
    default is NO_WRAP
    flex-wrap: wrap; wraps content from top to bottom
    flex-wrap: wrap-reverse; wraps content from bottom to top

flex-flow
    shorthand version of flex-direction and flex-wrap
    flex-flow: row wrap;
    flex-flow: column wrap;

justify-content
    main-axis
    default value is always flex-start
    flex-start, flex-end, center, space-around, space-between, space-evenly;

align-items
    cross-axis/up and down vertical
    cross-axis is perpendicular to the main-axis
    any time align is used it will be on the cross axis
    stretch is the default value
    stretch, flex-start, flex-end, center, baseline

align-content
    similar to how justify-content works for the main axis
    still on the cross-axis
    default is still stretch
    stretch, flex-start, flex-end, center, space-between, space-around

You can use multiple properties when using flexbox
example:
    .example-centering {
        display: flex;
        justify-content: center;
        align-items: center;
    }