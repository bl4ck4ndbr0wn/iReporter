import { Component } from "../common/App";
import { auth_login_elements } from "../common/Elements";
import Api from "../api/index";

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

export default Login;
