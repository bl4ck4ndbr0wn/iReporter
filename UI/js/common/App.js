class Component {
  constructor() {
    this.setState = this.setState.bind(this);
  }

  setState(newState) {
    return Object.assign(this.state, newState);
  }
}

document.getElementById("popupCloseButton").addEventListener("click", e => {
  e.preventDefault();

  const alert = document.getElementById("popupmessage");
  alert.style.display = "none";
});
