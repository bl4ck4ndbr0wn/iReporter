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
    this.api.get(this.url).then(resp => {
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
