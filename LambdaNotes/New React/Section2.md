# Section 2
# Composing React Components and Passing Data Via Props
  Imports and Exports
    
    export const emphasize = str => {
      return str.toUpperCase();
    } // Exports a single named function

    const emphasize = str => {
      return str.toUpperCase();
    }

    export default emphasize; 

  Import Examples

    import { a } from './directory/fileName' // Single named export

    import { item1, item2, item3 } from './directory/filename' // Multi named exports

    import Component from './folderName/Component.js' // Exported as default

  File Path specification
    The prefixing `'./'` on the file URL points to a unique location of your file system. It indicates the file for import is exported in the current directory.
    `'../'` Indicates a location one directory higher.

    Current Directory == ./
    Parent Directory == ../
    Parent of Parent == ../../

# React Components to build a UI
  Nesting components

    const App = props => {
      return (
        <div>
          <h2>Hello world from, {props.name}</h2>
          <div>
            <h4>My best friend in this world is: {props.bestFriend}</h4>
            <p>My favorite book is: {props.favoriteBook}</p>
          </div>
        </div>
      );
    }

  Lets break this component down

    const Book = props => <p>My favorite book is: {props.favoriteBook}</p>

    const BestFriend = props => {
      return (
        <div>
          <h4>My best friend in this world is: {props.bestFriend}</h4>
          <Book favoriteBook={props.favoriteBook} />
        </div>
      )
    }

    const App = () => {
      return (
        <div>
          <BestFriend bestFriend="Homer Hickam" favoriteBook="October Sky"/>
        </div>
      );
    }

  Now lets build a few container components that each render their own children and grand children.

    const simpsonData = {
      name: "Orville Simpson",
      spouse: "Yuma Hickman",
      children: [
        {
          name: "Abraham Simpson",
          spouse: "Mona",
          children: [
            {
              name: "Homer Simpson",
              spouse: "Marge Bouvier",
              children: [
                {
                  name: "Bart Simpson"
                },
                {
                  name: "Lisa Simpson"
                },
                {
                  name: "Maggie Simpson"
                }
              ]
            }
          ]
        }
      ]
    };

  Parent component