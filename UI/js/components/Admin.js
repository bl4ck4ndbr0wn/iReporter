// Initializing the classes
const api = new Api();
const record = new Record();
const elements = edit_incident_status_elements();

const popupform = document.getElementById("editStatusForm");
const edit = document.getElementById("editRecord");
const alert = document.getElementById("popupmessage");
const message = document.getElementById("popuptextmsg");
const divpop = document.getElementById("popupdiv");

const data = {};

function componentDidMount() {
  api
    .get("/interventions")
    .then(resp => {
      Object.values(resp.data).map(list => {
        record.tableItem(list);
      });
    })
    .catch(error => {
      console.log(error);
    });
}

// single_record events

function editIncidentRecord(id) {
  console.log(id);

  popupform.style.display = "block";

  api.get(`/interventions/${id}`).then(resp => {
    console.log(resp.data);

    elements.status.addEventListener("change", e => {
      e.preventDefault();
      if (resp.data.record_type == "red-flag") {
        api
          .patch(`/red-flags/${id}/status`, {
            status: e.target.value
          })
          .then(r => {
            alert.style.display = "block";

            if (r.status === 202) {
              divpop.style.boxShadow = "10px 10px 60px green";
              message.style.color = "green";
              message.innerText = r.data[0].message;

              window.setTimeout(function() {
                alert.style.display = "none";
              }, 500);
            } else {
              divpop.style.boxShadow = "10px 10px 60px red";
              message.style.color = "red";
              message.innerText = r.error;
            }
          });
      } else if (resp.data.record_type == "intervention") {
        api
          .patch(`/interventions/${id}/status`, {
            status: e.target.value
          })
          .then(r => {
            alert.style.display = "block";

            if (r.status === 202) {
              divpop.style.boxShadow = "10px 10px 60px green";
              message.style.color = "green";
              message.innerText = r.data[0].message;

              window.setTimeout(function() {
                alert.style.display = "none";
              }, 500);
            } else {
              divpop.style.boxShadow = "10px 10px 60px red";
              message.style.color = "red";
              message.innerText = r.error;
            }
          });
      }
    });
  });
}

function deleteIncidentRecord(id) {
  console.log("deleting");
  api.delete(`/interventions/${id}`).then(r => {
    alert.style.display = "block";

    if (r.status === 200) {
      divpop.style.boxShadow = "10px 10px 60px green";
      message.style.color = "green";
      message.innerText = r.data[0].message;

      window.setTimeout(function() {
        alert.style.display = "none";
        window.location.reload();
      }, 1000);
    } else if (r.status === 401) {
      divpop.style.boxShadow = "10px 10px 60px red";
      message.style.color = "red";
      message.innerText = r.message;
    }
  });
}

document.getElementById("popupCloseButton2").addEventListener("click", e => {
  e.preventDefault();

  popupform.style.display = "none";
  window.setTimeout(function() {
    window.location.reload();
  }, 500);
});

// Alerts
document.getElementById("popupCloseButton").addEventListener("click", e => {
  e.preventDefault();

  const alert = document.getElementById("popupmessage");
  alert.style.display = "none";
});
componentDidMount();
