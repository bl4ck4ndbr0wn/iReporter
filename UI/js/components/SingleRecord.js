class SingleRecord extends Component {
  constructor() {
    super();
    this.state = {
      data: {}
    };
    this.api = new Api();
    this.record = new Record();
  }
  componentDidMount() {
    const number = this.getUrlVars()["id"];
    if (number > 0) {
      this.api.get(`/interventions/${number}`).then(resp => {
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
}

// Initializing the classes
const single_record = new SingleRecord();

// single_record events
single_record.componentDidMount();
