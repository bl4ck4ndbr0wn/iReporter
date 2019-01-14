class Register extends Component {
  constructor(props) {
    super(props);
    this.state = {
      firstname: "",
      lastname: "",
      othernames: "",
      email: "",
      phoneNumber: "",
      username: "",
      password: "",
      password_confirm: "",
      errors: {}
    };

    this.url = "/auth/signup";
    this.api = new Api();
    this.elements = auth_register_elements();

    this.onChange = this.onChange.bind(this);
    this.changeEventHandler = this.changeEventHandler.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  onChange() {
    Object.values(this.elements).map(el => {
      el.onchange = this.changeEventHandler;
    });
  }

  changeEventHandler(event) {
    console.log({ [event.target.name]: event.target.value });

    this.setState({ [event.target.name]: event.target.value });
  }

  onSubmit() {
    const errors = { ...this.state.errors };
    const { register_submit } = this.elements;
    register_submit.addEventListener("click", e => {
      e.preventDefault();

      let data = this.state;

      delete data["errors"];

      this.api
        .post(this.url, data)
        .then(r => {
          const alert = document.getElementById("popupmessage");
          const message = document.getElementById("popuptextmsg");
          const divpop = document.getElementById("popupdiv");

          alert.style.display = "block";
          message.innerText = r;

          if (r.status === 201) {
            divpop.style.boxShadow = "10px 10px 60px green";
            message.style.color = "green";
            message.innerText = r.data[0].message;
            window.setTimeout(function() {
              window.location = `${
                window.location.origin
              }/iReporter/UI/login.html`;
            }, 3000);
          } else if (r.status === 404) {
            divpop.style.boxShadow = "10px 10px 60px red";
            message.style.color = "red";
            Object.values(r.message).forEach(element => {
              message.innerText = element;
            });
          } else {
            divpop.style.boxShadow = "10px 10px 60px red";
            message.style.color = "red";
            message.innerText = r.data[0].message;
          }

          return r;
        })
        .catch();
    });
  }
}

// Initializing the classes
const register = new Register();

// Register events
register.onChange();
register.onSubmit();

// Alerts
document.getElementById("popupCloseButton").addEventListener("click", e => {
  e.preventDefault();

  const alert = document.getElementById("popupmessage");
  alert.style.display = "none";
});

if (
  window.location.pathname === "/iReporter/UI/register.html" &&
  localStorage.jwtToken
) {
  window.location = `${window.location.origin}/iReporter/UI/index.html`;
}
