class Api {
  constructor() {
    this.apiURL = "https://ireporter2018v2.herokuapp.com/api/v2";
  }

  logError(err) {
    console.log("Looks like there was a problem: \n", error);
  }

  validateResponse(resp) {
    if (!response.ok) {
      throw Error(response.statusText);
    }
    return response;
  }

  readResponseAsJSON(resp) {
    return resp.json();
  }

  get(endpoint) {
    const URL = `${this.apiURL}${endpoint}`;
    return fetch(URL)
      .then(this.validateResponse)
      .then(this.readResponseAsJSON)
      .catch(this.logError);
  }
}

module.exports = Api;
