[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b1ec3d9cd8264734bfaa9a81de17e57b)](https://app.codacy.com/app/bl4ck4ndbr0wn/iReporter?utm_source=github.com&utm_medium=referral&utm_content=bl4ck4ndbr0wn/iReporter&utm_campaign=Badge_Grade_Dashboard)
# IReporter [![codecov](https://codecov.io/gh/bl4ck4ndbr0wn/iReporter/branch/develop/graph/badge.svg)](https://codecov.io/gh/bl4ck4ndbr0wn/iReporter)  [![Build Status](https://travis-ci.org/bl4ck4ndbr0wn/iReporter.svg?branch=develop)](https://travis-ci.org/bl4ck4ndbr0wn/iReporter) ![license](https://img.shields.io/github/license/mashape/apistatus.svg) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/bl4ck4ndbr0wn/iReporter)
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

To view postman collection 

[Postman Api Collection](https://documenter.getpostman.com/view/3130673/RzfdpVp3)
and
[Heroku Api](https://documenter.getpostman.com/view/3130673/RzfdpVp3)

**How it works**
- Users can create an account and log in.
- Users can create a red-flag record (An incident linked to corruption).
- Users can create intervention record (a call for a government agency to intervene e.g repair bad road sections, collapsed bridges, flooding e.t.c).
- Users can edit their red-flag or intervention records.
- Users can delete their red-flag or intervention records.
- Users can add geolocation (Lat Long Coordinates) to their red-flag or intervention records.
- Users can change the geolocation (Lat Long Coordinates) attached to their red-flag or intervention records.
- Admin can change the status of a record to either under investigation, rejected (in the event of a false claim) or resolved (in the event that the claim has been investigated and resolved).
- Users can add images to their red-flag or intervention records, to support their claims.
- Users can add videos to their red-flag or intervention records, to support their claims.
- The application should display a Google Map with Marker showing the red-flag or intervention location.
- The user gets real-time email notification when Admin changes the status of their record.
- The user gets real-time SMS notification when Admin changes the status of their record.



## Installation and Deployment.

**Clone the repo**

```.env
 git clone https://github.com/bl4ck4ndbr0wn/iReporter.git
```

**Setup environment**

Create a virtualenvironment and activate it
 ```.env
 python3 - m venv env
 ```
 Create a ```.env``` file in the parent directory and add this:
 ```..env
 source env/bin/activate

 export FLASK_APP=run.py
       FLASK_CONFIG="development"
       FLASK_ENV=development
       FLASK_DEBUG=1
       JWT_SECRET_KEY="fkjsahgufhdsifshyc7r843cn74rn8"
 ```
 To initialize your flask environment and add environment variables to it run:
 ```.env
 source .env
 ```
 Install all the dependencies needed by
 ```..env
 pip install - r Requirements.txt
 ```
 **Run the application**
 
 Run the flask application
 ```.env
  flask run
 ```
 
**Test the application**
 ```.env
flask test 
or 
flask cov
```
 
## Endpoints to test

| Method | Endpoint                                    | Description                                    |
| ------ | ------------------------------------------- | ---------------------------------------------- |
| POST   | /api/v1/auth/signup                         | sign up a user                                 |
| POST   | /api/v1/auth/login                          | login a user                                   |
| POST   | /api/v1/red-flags                           | Create a red-flag record.                      |
| GET    | /api/v1/red-flags                           | Fetch all red-flag records.                    |
| GET    | /api/v1/red-flags/<red-flag-id>             | Fetch a specific red-flag record.              |
| PATCH  | /api/v1/red-flags/<red-flag-id>/location    | Edit the location of a specific record.        |
| PATCH  | /api/v1/red-flags/<red-flag-id>/comment     | Edit the comment of a specific record.         |
| DELETE | /api/v1/red-flags/<red-flag-id>             | Delete a specific red flag record.             |

### Author

Alpha Ng'ang'a