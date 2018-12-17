class CreateIncident extends Component {
  constructor(props) {
    super(props);
    this.state = {
      title: "",
      record_type: "intervention",
      location: "",
      comment: "",
      status: "draft",
      errors: {}
    };
    this.url = "/interventions";
    this.api = new Api();
    this.elements = incident_record_elements();

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
    const { incident_submit } = this.elements;
    incident_submit.addEventListener("click", e => {
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
          console.log(r);

          if (r.status === 201) {
            divpop.style.boxShadow = "10px 10px 60px green";
            message.style.color = "green";
            message.innerText = r.message;
            window.setTimeout(function() {
              window.location = `${window.location.origin}/UI/records.html`;
            }, 1000);
          } else if (r.error) {
            divpop.style.boxShadow = "10px 10px 60px red";
            message.style.color = "red";
            message.innerText = r.error;
          } else if (r.message) {
            divpop.style.boxShadow = "10px 10px 60px red";
            message.style.color = "red";
            Object.keys(r.message).forEach(key => {
              message.innerText = `${key}: ${r.message[key]}`;
            });
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
const createIncident = new CreateIncident();

// create Incident events
createIncident.onChange();
createIncident.onSubmit();

// Alerts
document.getElementById("popupCloseButton").addEventListener("click", e => {
  e.preventDefault();

  const alert = document.getElementById("popupmessage");
  alert.style.display = "none";
});
