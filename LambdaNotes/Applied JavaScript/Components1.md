> Components are the building blocks of modern aapplications.

A component is made up of several parts, HTML, CSS, and JS brought together for reuse in a website or application.

Writing CSS for components is more about a mentality than syntax.
Components should be modular and stand alone.

Make component styling not rely on any other styles.

If using a preprocessor a common practice is to have your preprocessed file named after the components.

JS is used to consume the data and output the content into the DOM.

    const buttons = document.querySelectorAll('.button');
    class Button {
      constructor(element){
        this.element = element;
        this.element.addEventListener('click', () => { this.buttonClick() });
      }
      buttonClick(event){
        console.log('button clicked!');
      }
    }