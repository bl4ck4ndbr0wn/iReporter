# IReporter Api Endpoints

## Prerequisites

- Python3 - A programming language that lets us work more quickly (The universe loves speed!).
- Flask - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
- Virtualenv - A tool to create isolated virtual environments

### Virtual Environment

We first create this applications directory. On the terminal, create an empty directory called bucketlist with `mkdir iReporter_APi` in your prefered destination directory. Then, Cd into the directory. Create an isolated virtual environment: `$ virtualenv env or python3 -m venv env`

Install Autoenv globally using `pip3 install autoenv` Here's why – Autoenv helps us to set commands that will run every time we `cd` into our directory. It reads the `.env` file and executes for us whatever is in there.

## To run the application

Simply source the .env file and the app will start in development mode.
`$ source .env`

### Install dependancies

After runing the above command,
`(venv)$ pip install flask`

Thats it. You are all set :bowtie:
