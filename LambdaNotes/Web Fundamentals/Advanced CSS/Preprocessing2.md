Parametric Mixins, functions, escaping and Importing

Parametric Mixins use arguments and parameters in their syntax. Here is a standard mixin:
    .center(){
        display: flex;
        justify-content: center;
        align-items: center;
    }
    // usage
    .center();

This way of doing a mixin is very rigid and only allows for centering of a item.
Incorporating parameters and arguments allows for a much broader use of the mixin for different situations

    .center(@justify, @align){
        display: flex;
        justify-content: @justify;
        align-items: @align;
    }

    //usage 
    .center(flex-start, center);

parametric even allows for defaults to be used.

    .center(@justify: center, @align: center){
        display: flex;
        justify-content: @justify;
        align-items: @align;
    }

    //usage
    .center(@justify, @align);

Functions are pre-built pieces of code from the LESS library itself.

View all available functions here: http://lesscss.org/functions/

most used on hover effects right now
    background-color: darken(teal, 5%)
    background-color: lighten(teal, 5%)


Escaping is used for variables to hold a string value. Most widely used for media queries.

    @tablet: ~"(max-width: 500px)";
    @desktop: ~"(max-width: 800px)";


Imports allow for multiple people to work on the same project but work on different sections of the css and allow for easier commits and less commit errors.
Breaks down the css into much more manageable pieces for each section of content.

with Importing the Cascade MATTERS.

always import variables and mixins first, then general styles then your page components.