import React, { Component } from 'react';

export class Todo extends Component {
  constructor() {
    super();
    this.state = {
      todos: [],
      newTodo: ''
    }
  }

  handleChange(e) {
    const { value } = e.target;
    this.setState({ newTodo: value })
  }

  handleClick(e) {
    e.preventDefault();
    const todos = [...this.state.todos, this.state.newTodo]
    this.setState({ todos, newTodo: '' })
  }

  render() {
    return (
      <div>
        <form onSubmit={e => this.handleClick(e)}>
          <input value={this.state.newtodo} onChange={(e) => this.handleChange(e)} type="text" placeholder="New Todo" />
          <button>Click</button>
        </form>
        <ul>
          {this.state.todos.map(todo => <li>{todo}</li>)}
        </ul>
      </div>
    );
  }
}
