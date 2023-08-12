# Setup guide

### Requirements:

- Postgres
- Python version `3.8^`
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

### Modify env

Update the `.env` file to match your db url. ex:\
`DATABASE_URL=postgresql:///career_zen` \
or\
`DATABASE_URL=postgresql://postgres:123456@localhost:5432/career_zen?options=-csearch_path%3Dcareer_zen`

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
