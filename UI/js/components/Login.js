class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "alpha",
      password: "Ak3Swal(",
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

      delete data["errors"];

      this.api
        .post(this.url, data)
        .then(r => {
          const alert = document.getElementById("popupmessage");
          const message = document.getElementById("popuptextmsg");
          const divpop = document.getElementById("popupdiv");

          alert.style.display = "block";

          if (r.status === 200) {
            divpop.style.boxShadow = "10px 10px 60px green";
            message.style.color = "green";
            message.innerText = r.data[0].message;
            // Save token  to localStorage
            const { token } = r;
            // Set token to ls
            localStorage.setItem("jwtToken", token);
            // Check for token
            if (localStorage.jwtToken) {
              window.setTimeout(function() {
                window.location = `${window.location.origin}/UI/records.html`;
              }, 1000);
            }
          } else {
            divpop.style.boxShadow = "10px 10px 60px red";
            message.style.color = "red";
            message.innerText = r;
          }

          return r;
        })
        .then(r => {
          console.log(r);
        })
        .catch();
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

if (window.location.pathname === "/UI/login.html" && localStorage.jwtToken) {
  window.location = `${window.location.origin}/UI/index.html`;
}
