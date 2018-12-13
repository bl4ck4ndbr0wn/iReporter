class AllRecords extends Component {
  constructor() {
    super();
    this.state = {
      data: {}
    };
    this.url = "/interventions";
    this.api = new Api();
    this.record = new Record();
  }

  componentDidMount() {
    console.log("getting all records");
    this.api.get(this.url).then(resp => {
      console.log(resp);
      Object.values(resp.data).map(list => {
        this.record.recordList(list);
      });
    });
  }
}

// Initializing the classes
const allRecords = new AllRecords();

// AllRecords events
allRecords.componentDidMount();
