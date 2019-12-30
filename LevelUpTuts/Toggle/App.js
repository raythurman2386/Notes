import React from 'react'
import Toggle from 'Toggle'

const App = () => {
  return (
    <div>
      <Toggle>
        {({ on, toggle }) => (
          <>
            {on &&
              (
                <ul>
                  <li>Menu</li>

                  <li>Menu</li>
                  <li>Menu</li>

                </ul>
              )}
            <button onClick={toggle}>Show / Hide</button>
          </>
        )}
      </Toggle>
    </div>
  )
}

export default App
