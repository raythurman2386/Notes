# Composing React Components and Passing Data Via Props
# Imports and Exports
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

# What are Props
  React utilizes a top to bottom strategy when passing data. We know about state and how to implement it into an application using the state hook. Now we're going to take a look at what we can do with that data.

  When we want to pass information held on state inside one component to another component, we pass it as props. We never make changes to props data - props are read only

  A `stateful` component is one that holds state data, either as an object or a function component that includes the useState function made available in the React v16.8 release.

  When data comes into our app, it is loaded and stored on state, either in a centralized component specifically for state management, or a component rendering other components.

  Components rendered in a stateful component can receive that state data via a props attribute. Here it can be sent down on the props object to the child component, and there we can access it just like we would with most any other object.

    // const user = { name: 'Raymond', age: 30 };

    const App = () => {
      // same as above except using a hook
      const [user, setUser] = useState({name: 'Raymond', age: 30});

      return <UserInfo user={user} />
    }

    const UserInfo = props => {
      return {
        <div>
          <DisplayName user={props.user} />
          <DisplayAge user={props.user}>
        </div>
      }
    }

    const DisplayName = props => {
      return (
        <div>
          <h2>Hello, my name is {props.user.name}.</>
          <h3>My age is {props.user.age}.</h3>
        </div>
      )
    }

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
  Destructuring can also be used in place of props like so

    const Book = ({ favoriteBook }) => <p>My favorite book is: {favoriteBook}</p>

    const BestFriend = ({ bestFriend, favoriteBook }) => {
      return (
        <div>
          <h4>My best friend in this world is: {bestFriend}</h4>
          <Book favoriteBook={favoriteBook} />
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

    const Parent = props => {
      return (
        <div>
          <h1>Parent: {props.name}</h1>
          {props.child ? <Child name={props.child} /> : null}
          // If a child exists, Render the child
        </div>
      );
    };

  Child Component

    const Child = props => {
      return (
        <div>
          <h2>Child: {props.name}</h2>
          {props.grandChild ? <GrandChild name={props.grandChild} /> : null}
          // If GrandChild exists render grandchild
        </div>
      )
    }

  GrandChild Component

    const GrandChild = props => {
      return (
        <div>
          <h3>{props.name}</h3>
        </div>
      );
    }

    <Parent
      name={simpsonData[0].name}
      child={simpsonData[0].children[0].name}
      grandChild={simpsonData[0].children[0].children[0].name}
    />

  Thurman Data

    const thurmanData = {
      name: "Tom Thurman",
      spouse: "Beth Thurman",
      children: [
        {
          name: "Mallory Korte",
          spouse: "Brandon Korte",
          children: [
            {
              name: "Logan Stowers"
            },
            {
              name: "Avaya Korte"
            }
          ]  
        },
        {
          name: "Raymond Thurman",
          spouse: "Sheryl Thurman",
          children: [
            {
              name: "Melody Thurman"
            },
            {
              name: "Bradley Thurman"
            }
          ]
        }
      ]
    };

# Pass props as dynamic data
    import React, { useState } from "react";

    function App() {
      const [color, setColor] = useState("#FFFFFF");

      const changeColor = array => {
        setColor(array[Math.floor(Math.random() * array.length)]);
      }

      return (
        <div className="App">
          <Button color={color} changeColor={changeColor} />
        </div>
      );
    }

    const Button = props => {
      const colors = [
        "#FFBAAA",
        "#27576B",
        "#D47F6A",
        "#AA7539",
        "#003D19",
        "#6E91A1",
        "#552D00"
      ];

      return (
        <button
          style={{ background: props.color, height: '50px', width: '200px'}}
          onClick={()=>props.changeColor(colors)}
        >
          Click Me!
        </button>
      )
    }

# Styling with CSS and SASS
  Inline CSS - inline styling with the `style` attribute is spectified as an object with the style name in camelCase and the value set to a string

    <h1 style={{fontSize: "30px" }}>Inline Style Syntax</h1>

  Regular CSS

    <h1 className="header">CSS Style Syntax</h1>

    .header {
      color: gray;
    }

    <h1 className={props.isActive ? 'active' : ''}>Dynamic class name</h1>

# SASS
  Sass is style sheet language, or preprocessor scripting language, that will compile to CSS. Sass is now available feature with react-scripts@2.0.0 and higher

    npm install node-sass

  Once complete, all you need to do is start making style files with the `.sass` extension for Sass and `.scss` for the newest syntax  

  Sass vs Scss - The difference is syntax;
  Sass is structured off of indentations and omits brackets and semicolons. It can make for a very clean and easy to read code base, however the simplicity can lead to excessive nesting and less structure isn't always desirable.

  Scss is almost identical to vanilla css, which makes the transition almost seamless. You're gaining all the special abilities of Sass but without having to rewrite your code.