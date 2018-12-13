class Component {
  constructor() {
    this.setState = this.setState.bind(this);
  }

  setState(newState) {
    return Object.assign(this.state, newState);
  }
}

class Api {
  constructor() {
    this.apiURL = "https://ireporter2018v2.herokuapp.com/api/v2";
  }

  logError(err) {
    console.log("Looks like there was a problem: \n", error);
  }

  readResponseAsJSON(resp) {
    return resp.json();
  }

  get(endpoint) {
    const URL = `${this.apiURL}${endpoint}`;
    return fetch(URL, {
      method: "GET",
      mode: "cors",
      cache: "default"
    })
      .then(this.validateResponse)
      .then(this.readResponseAsJSON)
      .catch(this.logError);
  }

  post(endpoint, data) {
    const URL = `${this.apiURL}${endpoint}`;
    console.log(URL);

    return fetch(URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then(this.readResponseAsJSON)
      .catch(this.logError);
  }
}

const authForm = document.forms.auth_form;
const {
  auth_firstname,
  auth_lastname,
  auth_othername,
  auth_username,
  auth_email,
  auth_password,
  auth_confirm_password,
  login_submit,
  register_submit
} = authForm.elements;

const auth_register_elements = () => {
  return {
    auth_firstname,
    auth_lastname,
    auth_othername,
    auth_username,
    auth_email,
    auth_password,
    auth_confirm_password,
    register_submit
  };
};

const auth_login_elements = () => {
  return {
    auth_username,
    auth_password,
    login_submit
  };
};

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

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: "",
      errors: {}
    };

    this.url = "/auth/signin";
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

      console.log(data);
      // this.api.post(this.url, this.state);
    });
  }
}

if (window.location.pathname === "/UI/register.html") {
  // Initializing the classes
  const register = new Register();

  // Register events
  register.onChange();
  register.onSubmit();
} else if (window.location.pathname === "/UI/login.html") {
  // Initializing the classes
  const login = new Login();

  // login events
  login.onChange();
  login.onSubmit();
}
document.getElementById("popupCloseButton").addEventListener("click", e => {
  e.preventDefault();

  const alert = document.getElementById("popupmessage");
  alert.style.display = "none";
});
