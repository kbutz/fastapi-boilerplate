# fastapi-boilerplate 

A project for me to try out fastapi+mysql by building a production ready boilerplate.

To run locally, 
- spin up a virtualenv `virtualenv -p python3.7 vent` and `.venv/bin/activate` or `source venv/bin/activate`
- `pip install -r requirements.txt`
- `uvicorn main:app --reload`

TODO: 
- [x] Basic route structure for a FastAPI app w/ multiple routers
- [x] sql-alchemy integration
- [x] Add migrations
- [x] Migrations need to have their config set from the global config
- [ ] Follow up for migrations: review developer workflow for migrations, refactor to make it more ergonomic if needed. 
      The migrations step should be as simple as Go's gorm.Automigrate - define a model, 
      let the service update the DB schema on startup
- [ ] Test coverage, figure out how to write integration tests for FastAPI routes
- [ ] Dockerfile for deployment
- [ ] Travis or CircleCI integration
- [ ] Metrics and observation
- [ ] Documentation on the fastapi boilerplate workflow

 
