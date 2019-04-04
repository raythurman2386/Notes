Desktops and laptops should be at least 1024x768 pixels or higher.

Most common breakpoints for mobile design

    /* start of desktop styles */

    @media screen and (max-width: 991px) {
    /* start of large tablet styles */

    }

    @media screen and (max-width: 767px) {
    /* start of medium tablet styles */

    }

    @media screen and (max-width: 479px) {
    /* start of phone styles */

    }

Use these snippets as a guide and customize as needed.

1em = 10px to set the font size to the default 14px you would have to use 1.4em.

em based font-sizing compounds. Meaning a list within a list isn't 14px it would be 20 pixels. Go another level deeper such as a list within a list and the font
would be 27px.

this is where rem comes in to play.

rem means root em
rem unit is relative to the root--or the html--element. which means you can define a single font size on the html element and define all rem units to be a percentage of that.
    html { font-size: 62.5%; }
    body { font-size: 14px; font-size: 1.4rem; } == 14px
    h1 { font-size: 24px; font-size: 2.4rem; } == 24px

    TL/DR

        pixels are ignorant, don't use them anymore
        Use REMs for sizes and spacing
        Use EMs for media queries