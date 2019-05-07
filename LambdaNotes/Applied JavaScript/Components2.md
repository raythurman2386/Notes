Data Attributes

Data attributes give developers another way to hook into the DOM without having to use classes and IDs

HTML5 standard allows us to add our own attributes, preceded by data-

This allows us to pass info from our HTML to JS or CSS

    <div data-school="Lambda" class="school">Lambda School</div>

    div[data-school='Lambda']{
      /* CSS style rules here */
    }

  To access the data in javascript we use the .dataset property. This will return an Object

    const school = document.querySelector('.school');
    const schoolName = school.dataset.school;
    console.log(schoolName); // Lambda

  We can also use the data attribute in a css style selector

    const schoolElement = document.querySelector('div[data-school='Lambda']');