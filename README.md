# iReporter [![Build Status](https://travis-ci.org/bl4ck4ndbr0wn/iReporter.svg?branch=gh-pages)](https://travis-ci.org/bl4ck4ndbr0wn/iReporter) ![license](https://img.shields.io/github/license/mashape/apistatus.svg) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/bl4ck4ndbr0wn/iReporter)

iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

To view the site navigate to this url

[iReporter](https://bl4ck4ndbr0wn.github.io/iReporter/iReporter/UI)

### pivalal tracker IReport project stories

[Stories](https://www.pivotaltracker.com/projects/2226962)

## Project Overview

Corruption is a huge bane to Africa’s development. African countries must develop novel and
localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables
any/every citizen to bring any form of corruption to the notice of appropriate authorities and the
general public. Users can also report on things that needs government intervention.

## Features

1. Users can create an account and log in.
2. Users can create a red-flag record (An incident linked to corruption).
3. Users can create intervention record (a call for a government agency to intervene e.g
   repair bad road sections, collapsed bridges, flooding e.t.c).
4. Users can edit their red-flag or intervention records.
5. Users can delete their red-flag or intervention records.
6. Users can add geolocation (Lat Long Coordinates) to their red-flag or intervention
   records.
7. Users can change the geolocation (Lat Long Coordinates) attached to their red-flag or
   intervention records.
8. Admin can change the status of a record to either under investigation, rejected (in the
   event of a false claim) or resolved (in the event that the claim has been investigated and
   resolved).

#### To run the code just run:

```
npm install -g live-server

git clone {url}
cd into iReporter

live-server UI/
```

The results are shown in the browser's console.

**Test the application**

```.env
npm install

npm test

or

npm run coveralls
```

## License

MIT License
@2018 Alpha Nganga Ndirangu
