class Profile extends Component {
  constructor() {
    super();
    this.state = {
      firstname: "",
      lastname: "",
      othernames: "",
      email: "",
      phoneNumber: ""
    };
    this.url = "/profile";
    this.api = new Api();
    this.elements = profile_elements();

    this.onChange = this.onChange.bind(this);
    this.changeEventHandler = this.changeEventHandler.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  componentDidMount() {
    api.get(this.url).then(r => {
      console.log(r);
    });
  }

  update() {
    const profilename = document.getElementById("profileName");
  }

  onChange() {
    Object.values(this.elements).map(el => {
      el.onchange = this.changeEventHandler;
    });

    console.log(this.state);
  }

  changeEventHandler(event) {
    console.log({ [event.target.name]: event.target.value });

    this.setState({ [event.target.name]: event.target.value });
  }
  onSubmit() {
    const { profile_submit } = this.elements;
    profile_submit.addEventListener("click", e => {
      e.preventDefault();

      let data = this.state;

      this.api
        .patch(this.url, data)
        .then(r => {
          const alert = document.getElementById("popupmessage");
          const message = document.getElementById("popuptextmsg");
          const divpop = document.getElementById("popupdiv");

          alert.style.display = "block";

          if (r.status === 202) {
            divpop.style.boxShadow = "10px 10px 60px green";
            message.style.color = "green";
            message.innerText = r.data[0].message;
            window.setTimeout(function() {
              window.location = `${window.location.origin}/UI/profile.html`;
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
            message.innerText = r.message;
          }

          return r;
        })
        .catch();
    });
  }
}

// Initializing the classes
const profile = new Profile();

// profile events
profile.componentDidMount();
profile.onChange();
profile.onSubmit();

// Alerts
document.getElementById("popupCloseButton").addEventListener("click", e => {
  e.preventDefault();

  const alert = document.getElementById("popupmessage");
  alert.style.display = "none";
});
