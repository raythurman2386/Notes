// TODO: for (var i = 0; i < 3; i++) {
//   setTimeout(function () { alert(i); }, 1000 + i);
// }

(function () {
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
