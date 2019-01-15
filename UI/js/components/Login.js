class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: "",
      errors: {}
    };

    this.url = "/auth/login";
    this.api = new Api();
    this.elements = auth_login_elements();

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
    const { login_submit } = this.elements;
    login_submit.addEventListener("click", e => {
      e.preventDefault();

      let data = this.state;

      login_submit.value = "Login in ...";

      delete data["errors"];

      this.api
        .post(this.url, data)
        .then(r => {
          const alert = document.getElementById("popupmessage");
          const message = document.createElement("div");

          if (r.status === 200) {
            // Save token  to localStorage
            const { token } = r;
            // Set token to ls
            localStorage.setItem("jwtToken", token);
            // Check for token
            if (localStorage.jwtToken) {
              alert.className =
                "alert alert-success alert-dismissible fade show";
              message.innerText = r.data[0].message;
              message.id = "popuptextmsg";
              alert.appendChild(message);

              window.setTimeout(function() {
                alert.style.display = "none";
              }, 3000);

              window.setTimeout(function() {
                redirect: window.location.replace("./records.html");
              }, 1900);
            }
          } else if (r.status === 400) {
            alert.className = "alert alert-danger alert-dismissible fade show";
            message.innerText = Object.values(r.message);
            message.id = "popuptextmsg";
            alert.appendChild(message);

            window.setTimeout(function() {
              alert.removeChild(message);
              alert.className = "alert alert-danger alert-dismissible fade ";

              login_submit.value = "Sign in";
            }, 3000);

            alert.className = "";
          } else if (r.status === 401) {
            alert.className = "alert alert-warning alert-dismissible fade show";
            message.innerText = r.data[0].message;
            message.id = "popuptextmsg";
            alert.appendChild(message);

            window.setTimeout(function() {
              alert.removeChild(message);
              alert.className = "alert alert-danger alert-dismissible fade ";

              login_submit.value = "Sign in";
            }, 3000);
          }
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
const login = new Login();

// login events
login.onChange();
login.onSubmit();

// Alerts
document.getElementById("popupCloseButton").addEventListener("click", e => {
  e.preventDefault();

  const alert = document.getElementById("popupmessage");
  alert.style.display = "none";
});

if (
  window.location.pathname === "/iReporter/UI/login.html" &&
  localStorage.jwtToken
) {
  redirect: window.location.replace("./index.html");
}
