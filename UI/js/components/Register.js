class Register extends Component {
  constructor(props) {
    super(props);
    this.state = {
      firstname: "dfgdfg",
      lastname: "dfgd",
      othernames: "dfgd",
      email: "dfgdf",
      phoneNumber: "dfgd",
      username: "dfgds6d",
      password: "dfgdf",
      password_confirm: "dfgd",
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
          message.innerText = r.data[0].message;

          if (r.status === 201) {
            divpop.style.boxShadow = "10px 10px 60px green";
            message.style.color = "green";

            window.setTimeout(function() {
              window.location = `${window.location.origin}/UI/login.html`;
            }, 3000);
          } else {
            divpop.style.boxShadow = "10px 10px 60px red";
            message.style.color = "red";
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
