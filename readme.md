# Setup guide

### Requirements:

- Postgres
- Python version `3.9^`
- IDE

## Setup

### Virtual env

Create virtual environment

`python -m venv venv`

activate the virtual env

`source venv/bin/activate` for linux and mac\
`venv\Scripts\activate` for windows

Install packages

`pip install -r requirements.txt`
`npm install`

Load CSS

`npm run tailwind`

### Modify env

Update the `.env` file to match your db url. ex:\
`DATABASE_URL=postgresql://postgres:123456@localhost:5432/database_name`

### Initialize db

Run the following commands to initliaze database

```
flask db init
flask db migrate
flask db upgrade
```

## Run

To run the appliaction first setup the `FLASK_APP=app.py` env then trigger `flask run`

```
export FLASK_APP=app.py
flask run
```
