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

      register_submit.value = "Creating User ...";

      delete data["errors"];

      this.api
        .post(this.url, data)
        .then(r => {
          const alert = document.getElementById("popupmessage");
          const message = document.createElement("div");

          alert.style.display = "block";
          message.innerText = r;

          if (r.status === 201) {
            alert.className = "alert alert-success alert-dismissible fade show";
            message.innerText = r.data[0].message;
            message.id = "popuptextmsg";
            alert.appendChild(message);

            window.setTimeout(function() {
              alert.style.display = "none";
            }, 3000);

            window.setTimeout(function() {
              redirect: window.location.replace("./login.html");
            }, 500);
          } else if (r.status === 400) {
            alert.className = "alert alert-danger alert-dismissible fade show";
            message.id = "popuptextmsg";

            Object.values(r.message).forEach(element => {
              message.innerText = element;
            });
            alert.appendChild(message);

            window.setTimeout(function() {
              alert.removeChild(message);
              alert.className = "alert alert-danger alert-dismissible fade ";

              register_submit.value = "Sign UP";
            }, 3000);
          } else {
            alert.className = "alert alert-danger alert-dismissible fade show";
            message.id = "popuptextmsg";
            message.innerText = r.data[0].message;
            alert.appendChild(message);

            window.setTimeout(function() {
              alert.removeChild(message);
              alert.className = "alert alert-danger alert-dismissible fade ";

              register_submit.value = "Sign UP";
            }, 3000);
          }

          return r;
        })
        .catch(error => {
          alert.className = "alert alert-danger alert-dismissible fade show";
          message.id = "popuptextmsg";
          message.innerText = error;
          alert.appendChild(message);

          window.setTimeout(function() {
            alert.removeChild(message);
            alert.className = "alert alert-danger alert-dismissible fade ";
          }, 3000);
        });
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
