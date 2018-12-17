class Api {
  constructor() {
    this.apiURL = "https://ireporter2018v2.herokuapp.com/api/v2";
  }

  logError(error) {
    console.log("Looks like there was a problem: \n", error);
  }

  readResponseAsJSON(resp) {
    return resp.json();
  }

  getAuthToken() {
    // Check for token
    if (localStorage.jwtToken) {
      return localStorage.jwtToken;
    }
    return null;
  }

  get(endpoint) {
    const URL = `${this.apiURL}${endpoint}`;
    let token = this.getAuthToken();

    let headers = { "Content-Type": "application/json" };
    if (token) {
      headers["Authorization"] = `Bearer ${token}`;
    }
    return fetch(URL, { headers })
      .then(this.readResponseAsJSON)
      .catch(this.logError);
  }

  post(endpoint, data) {
    const URL = `${this.apiURL}${endpoint}`;
    let token = this.getAuthToken();

    let headers = { "Content-Type": "application/json" };
    if (token) {
      headers["Authorization"] = `Bearer ${token}`;
    }
    return fetch(URL, {
      method: "POST",
      headers,
      body: JSON.stringify(data)
    })
      .then(this.readResponseAsJSON)
      .catch(this.logError);
  }

  patch(endpoint, data) {
    const URL = `${this.apiURL}${endpoint}`;
    let token = this.getAuthToken();

    let headers = { "Content-Type": "application/json" };
    if (token) {
      headers["Authorization"] = `Bearer ${token}`;
    }
    return fetch(URL, {
      method: "PATCH",
      headers,
      body: JSON.stringify(data)
    })
      .then(this.readResponseAsJSON)
      .catch(this.logError);
  }
}
