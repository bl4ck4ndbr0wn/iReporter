import { Component } from "../common/App";
import { auth_register_elements } from "../common/Elements";
import Api from "../api/index";

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
    const { submit } = this.elements;
    submit.addEventListener("click", e => {
      e.preventDefault();

      let data = this.state;

      console.log(data);
      // this.api.post(this.url, this.state);
    });
  }
}

export default Register;
