LESS is a CSS preprocessor. 
Less allows for things such as nesting, variables, mixins

LESS variables start with a @ sign
    @variable-name: #ff0000;
    @font-size: 16px;
    .some-class {
        font-size: @font-size;
        background: @variable-name;
    }

LESS Mixins derive their name from the ability to mix different classes together. Being able
to create one class and use it's properties within another class.

    .some-class {
        color: red;
        font-size: 14px;
    }

    .example-mixin {
        text-align: center;
        .some-class;
    }

    .font-class {
        color: black;
        font-size: 18px;
        text-align: center;
    }

    .box-class {
        width: 100px;
        height: 100px;
        background: gray;
    }

    .example-mixin {
        .font-class;
        .box-class;
    }

Nesting is extremely useful for organizing our code and keeping our specificity scoped properly. A good rule to follow is to avoid going more than 4 levels deep.

    .parent {
        color: black;
        font-size: 12px;

        .child {
            color: red;
            font-size: 16px;
        }  
    } // parent

Nested @ rule usage for media queries. Makes your code much more readable.
    .some-class {
        // Large screen styling
        width: 800px;
        height: 100%;
        background: gray;

        // Medium screen styling
        @media (max-width: 800px) {
            width: 100%;
            background: black;
        }

        // Small screen styling
        @media (max-width: 500px) {
            width: 80%;
            background: green;
        }
    }

LESS also allows for some simple mather operators such as + - * / on any number, color or variable
    .some-class {
        width: 100px + 10;  // 110px
    }
    .some-class {
        width: 100px - 10;  // 90px
    }
    .some-class {
        width: 100px * 10;  // 1000px
    }
    .some-class {
        width: 100px / 10;  // 10px
    }