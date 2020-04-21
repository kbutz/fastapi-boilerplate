# flask-boilerplate [![Build Status](https://travis-ci.org/kbutz/flask-boilerplate.svg?branch=master)](https://travis-ci.org/kbutz/flask-boilerplate)

Have trouble finding many simple resources between Flask's getting started, and Miguel Grinberg's awesome mega-tutorial,
I thought it would be useful to lay out a simple but easily extendable production ready project structure.

A simple scalable project structure for rest apis with python3, Flask + SQL-Alchemy, uWSGI, Docker with some examples of useful Flask 
patterns and config from json/environment variable for production deployment. Easily configurable locally with
local_settings.json, and easily deployed to any environment with Docker by injecting env variables.

Mostly a simplified version of Miguel Grinberg's Flask examples. 
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
- https://github.com/miguelgrinberg/flasky

Dockerfile based on @jfloff's alpine python examples:
- https://github.com/jfloff


To run with Docker:

- create config/local_settings.json from local_settings_sample.json
- If you don't have a mysql server running locally, you can spin up a mysql Docker container with a one line Docker command to get you started: `docker run --name mysql_container_name -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=example_db -p 3306:3306 -d mysql:5.7`
- `docker build -t flask-boilerplate -f ./deployment/Dockerfile.development .`
- `docker run -p 8000:8000 flask-boilerplate`

To run with dev server from virtualenv:
- virtualenv -p python3 .venv
- . .venv/bin/activate
- pip install -r requirements.txt
- uncomment `app.run(host='0.0.0.0', debug=True, port=8000)`
- python3 boilerplate.py


To run tests locally:
- from virtual-env, `python3 tests.py`
- Or, `docker build -t flask-boilerplate -f ./deployment/Dockerfile.test .`
- `docker run -e ENVIRONMENT='testing' flask-boilerplate`

To manage DB migrations with Flask-Migrate:
- NOTE: Flask-Migrate will look for app.py or wsgi.py by default. If your flask app exists in a different file, like in this boilerplate example, you'll need to either explicitly set the FLASK_APP env variable each time you run a flask migrate command, or set the env variable globally elsewhere.
- `FLASK_APP=boilerplate.py flask db init` # generates the alembic migration's folder
- `FLASK_APP=boilerplate.py flask db migrate` # generates the migration ddl in the versions package, captures changes by comparing against the connected DB
- `FLASK_APP=boilerplate.py flask db upgrade` # runs the migration ddls from the versions package

General notes on the workflow for DB schema migrations in this boilerplate:
 - To start fresh, delete the migrations folder and run `flask db init`, followed by `flask db migrate`. 
 - When you start the app, the upgrade command will run, running all available migration scripts in migrations/versions
 - To start from the existing migrations folder, first run the app which will run upgrade on your DB, 
 creating the DB and running all existing migrations.
 - For any future changes to your sql-alchemy db models, you'll need to run flask db migrate, adding the new 
 migration script. These will be applied to the app's target DB at startup,
 allowing you to run full schema migration in any environment, regardless of the current state of the 
 target DB. 
 - Note: if a target DB is out of sync with your migration scripts (e.g., you manually added or 
 removed a table/column), you could run into some issues (like dropping a column that doesn't exist). If this 
 occurs, you may need to remove the existing migration versions and rerun `flask db migrate` to generate
 the migration scripts bringing the schema up to date.
 - Note: Alembic will not catch all changes to your sql-alchemy models. It is important to review the auto-generated sql 
 and migration commands before applying to any target DB
 
 Note on uWSGI if deploying with multiple processes: you'll want to add `lazy-apps=true` to let uWSGI create the app instances post-fork to avoid sharing a single sql-alchemy db connection instance. Strange and unpleasant bugs will occur if you have multiple instances reusing the same sql-alchemy db instance.
