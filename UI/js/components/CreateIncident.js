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
    const { incident_submit } = this.elements;
    incident_submit.addEventListener("click", e => {
      e.preventDefault();

      incident_submit.value = "Creating new Incident ...";

      let data = this.state;

      delete data["errors"];

      this.api
        .post(this.url, data)
        .then(r => {
          const alert = document.getElementById("popupmessage");
          const message = document.createElement("div");

          if (r.status === 201) {
            alert.className = "alert alert-success alert-dismissible fade show";
            message.innerText = r.message;
            message.id = "popuptextmsg";
            alert.appendChild(message);

            window.setTimeout(function() {
              alert.style.display = "none";
            }, 3000);

            window.setTimeout(function() {
              redirect: window.location.replace("./records.html");
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

              register_submit.value = "Save New Record";
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
