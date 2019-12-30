// import React, { Component } from 'react'

// class Toggle extends Component {
//   state = {
//     on: false,
//   }

//   toggle = () => {
//     this.setState({
//       on: !this.state.on
//     })
//   }

//   render() {
//     return (
//       <div>
//         {this.state.on && <h1>Show Me</h1>}
//         <button onClick={this.toggle}>Show / Hide</button>
//       </div>
//     )
//   }
// }

// export default Toggle;

// import React, { Component } from 'react'

// class Toggle extends Component {
//   state = {
//     on: false,
//   }

//   toggle = () => {
//     this.setState({
//       on: !this.state.on
//     })
//   }

//   render() {
//     const { render } = this.props;

//     return (
//       <div>
//         {render({
//           on: this.state.on,
//           toggle: this.toggle
//         })}
//       </div>
//     )
//   }
// }

// export default Toggle;

import React, { Component } from 'react'

class Toggle extends Component {
  state = {
    on: false,
  }

  toggle = () => {
    this.setState({
      on: !this.state.on
    })
  }

  render() {
    const { children } = this.props;

    return children({
      on: this.state.on,
      toggle: this.toggle
    })
  }

}

export default Toggle;