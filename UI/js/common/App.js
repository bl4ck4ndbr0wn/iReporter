class Component {
  constructor() {
    this.setState = this.setState.bind(this);
  }

  setState(newState) {
    return Object.assign(this.setState, newState);
  }
}

module.exports = Component;
