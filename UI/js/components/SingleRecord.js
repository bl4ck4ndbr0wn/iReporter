class SingleRecord extends Component {
  constructor() {
    super();
    this.state = {
      data: {}
    };
    this.api = new Api();
    this.record = new Record();
    this.elements = edit_incident_elements();

    this.onChange = this.onChange.bind(this);
  }
  componentDidMount() {
    const number = this.getUrlVars()["id"];
    if (number > 0) {
      this.api.get(`/interventions/${number}`).then(resp => {
        this.setState({ data: resp.data });
        if (resp.status === 404) {
          const alert = document.getElementById("popupmessage");
          const message = document.getElementById("popuptextmsg");
          const divpop = document.getElementById("popupdiv");
          alert.style.display = "block";

          divpop.style.boxShadow = "10px 10px 60px green";
          message.style.color = "red";
          message.innerText = resp.data[0].message;

          window.setTimeout(function() {
            alert.style.display = "none";
          }, 1000);
          window.location = `${
            window.location.origin
          }/iReporter/UI/records.html`;
        }
        this.record.singleRecord(resp.data);
      });
    } else {
      window.setTimeout(function() {
        window.location = `${window.location.origin}/iReporter/UI/records.html`;
      }, 1000);
    }
  }

  getUrlVars() {
    let vars = {};
    let parts = window.location.href.replace(
      /[?&]+([^=&]+)=([^&]*)/gi,
      function(m, key, value) {
        vars[key] = value;
      }
    );
    return vars;
  }

  onChange() {
    const { comment, location } = this.elements;

    const number = this.getUrlVars()["id"];
    const alert = document.getElementById("popupmessage");
    const message = document.getElementById("popuptextmsg");
    const divpop = document.getElementById("popupdiv");

    if (number > 0) {
      //Edit comment
      comment.addEventListener("change", e => {
        e.preventDefault();

        this.api
          .patch(`/interventions/${number}/comment`, {
            comment: e.target.value
          })
          .then(r => {
            alert.style.display = "block";

            if (r.status === 200) {
              divpop.style.boxShadow = "10px 10px 60px green";
              message.style.color = "green";
              message.innerText = r.data[0].message;

              window.setTimeout(function() {
                alert.style.display = "none";
              }, 800);
            } else {
              divpop.style.boxShadow = "10px 10px 60px red";
              message.style.color = "red";
              message.innerText = `Comment: ${r.message.location}`;
            }
          });
      });

      // Edit location
      location.addEventListener("change", e => {
        e.preventDefault();

        this.api
          .patch(`/interventions/${number}/location`, {
            location: e.target.value
          })
          .then(r => {
            alert.style.display = "block";

            if (r.status === 202) {
              divpop.style.boxShadow = "10px 10px 60px green";
              message.style.color = "green";
              message.innerText = r.data[0].message;

              window.setTimeout(function() {
                alert.style.display = "none";
              }, 800);
            } else {
              divpop.style.boxShadow = "10px 10px 60px red";
              message.style.color = "red";
              message.innerText = `Location: ${r.message.location}`;
            }
          });
      });
    } else {
      window.setTimeout(function() {
        window.location = `${window.location.origin}/iReporter/UI/records.html`;
      }, 1000);
    }
  }

  editIncident() {
    console.log(this.state);

    const popupform = document.getElementById("popupform");
    const edit = document.getElementById("editRecord");
    const { comment, location } = this.elements;

    edit.addEventListener("click", e => {
      e.preventDefault();
      popupform.style.display = "block";

      comment.value = this.state.data.comment;
      location.value = this.state.data.location[0];
    });

    document
      .getElementById("popupCloseButton1")
      .addEventListener("click", e => {
        e.preventDefault();

        popupform.style.display = "none";
        window.setTimeout(function() {
          window.location.reload();
        }, 2000);
      });
  }
}

// Initializing the classes
const single_record = new SingleRecord();

// single_record events
single_record.componentDidMount();
single_record.editIncident();
single_record.onChange();
