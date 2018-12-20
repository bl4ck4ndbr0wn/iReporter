# IReporter [![Build Status](https://travis-ci.org/bl4ck4ndbr0wn/iReporter.svg?branch=develop-v2)](https://travis-ci.org/bl4ck4ndbr0wn/iReporter) [![Coverage Status](https://coveralls.io/repos/github/bl4ck4ndbr0wn/iReporter/badge.svg?branch=develop-v2)](https://coveralls.io/github/bl4ck4ndbr0wn/iReporter?branch=develop-v2)  ![license](https://img.shields.io/github/license/mashape/apistatus.svg) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/bl4ck4ndbr0wn/iReporter) [![Maintainability](https://api.codeclimate.com/v1/badges/23c79b32532f75cddbc0/maintainability)](https://codeclimate.com/github/bl4ck4ndbr0wn/iReporter/maintainability)
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

To view postman collection 

[Postman Api Documentation.](https://documenter.getpostman.com/view/3130673/RzfdpVp3)

[Heroku Application](https://ireporter2018v2.herokuapp.com)

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
 rename ```.env.example``` to```.env``` file in the parent directory and update it with the values you want.

 To initialize your flask environment and add environment variables to it run:
 ```.env
 source .env
 ```
 Install all the dependencies needed by
 ```..env
 pip install - r requirements.txt
 ```
 **Run the application**
 
 First Create a postgresql database table named ```ireporter```
 
 To create tables into that database run
 ```.env
flask migrate
```
To drop or delete tables from that table run:
```.env
flask drop
```
To create initial admin user run:
```.env
flask seed
```
 
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
*(url: http://localhost, http://127.0.0.1)*

| Method | Endpoint                                       | Description                                       |
| ------ | ---------------------------------------------- | ------------------------------------------------- |
| POST   | /api/v2/auth/signup                            | sign up a user                                    |
| POST   | /api/v2/auth/login                             | login a user                                      |
| POST   | /api/v2/interventions                          | Create a red-flag record.                         |
| GET    | /api/v2/interventions                          | Fetch all red-flag records.                       |
| GET    | /api/v2/intervention/<intervention-id>         | Fetch a specific red-flag record.                 |
| PATCH  | /api/v2/intervention/<intervention-id>/location| Edit the location of a specific record.           |
| PATCH  | /api/v2/intervention/<intervention-id>/comment | Edit the comment of a specific record.            |
| PATCH  | /api/v2/red-flags/<red-flag-id>/status         | Edit the status of an red-flag record. (Admin)    |
| PATCH  | /api/v2/interventions/<intervention-id>/status | Edit the status of an intervention record. (Admin)|
| DELETE | /api/v2/intervention/<intervention-id>         | Delete a specific red flag record.                |

### Author

Alpha Ng'ang'a
