// WEBAPI Questions
// 1. Two parts of express that I have learned about this week is middleware and Routers
// 2. Middleware is used to add additional functionality to an express application.
// 3. A resource is anything that is sent to or recieved from the API
// 4. An API can return a status code or a message back to the client to help clients know the request was successful
// 5. We can partition our application into sub-app by using express routers, and break the application down into smaller chunks so it's easier to work with.

// for (var i = 0; i < 3; i++) {
//   setTimeout(function () { alert(i); }, 1000 + i);
// }

(function() {
  var a = (b = 5);
})();

console.log(b);

// CamelCase
function camalize(str) {
  return str
    .toLowerCase()
    .replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => chr.toUpperCase());
}

console.log(camalize("How *are -You _doing"));

// state machine in JS
const machine = {
  dispatch(actionName, ...payload) {
    const actions = this.transitions[this.state];
    const action = this.transitions[this.state][actionName];

    if (action) {
      action.apply(machine, ...payload);
    }
  },
  changeStateTo(newState) {
    this.state = newState;
  },
  state: "idle",
  transitions: {
    idle: {
      click: () => {
        this.changeStateTo("fetching");
        service.getData().then(
          data => {
            try {
              this.dispatch("success", JSON.parse(data));
            } catch (error) {
              this.dispatch("failure", error);
            }
          },
          error => this.dispatch("failure", error)
        );
      }
    },
    fetching: {
      success: data => {
        this.changeStateTo("idle");
      },
      failure: err => {
        this.changeStateTo("error");
      }
    },
    error: {
      retry: () => {
        this.changeStateTo("idle");
        this.dispatch("click");
      }
    }
  }
};

machine.dispatch("click");
