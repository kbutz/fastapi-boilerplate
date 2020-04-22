# fastapi-boilerplate 

A project for me to try out fastapi+mysql by building a production ready boilerplate.

TODO: An introduction to the fastapi boilerplate project, steps to spin up, deploy and monitor a fastapi + mysql service.

TODO: 
- [x] Basic route structure for a FastAPI app w/ multiple routers
- [x] sql-alchemy integration
- [x] Add migrations
- [ ] Follow up for migrations: review developer workflow for migrations, refactor to make it more ergonomic if needed. 
      The migrations step should be as simple as Go's gorm.Automigrate - define a model, 
      let the service update the DB schema on startup
- [ ] Test coverage, figure out how to write integration tests for FastAPI routes
- [ ] Dockerfile for deployment
- [ ] Travis or CircleCI integration
- [ ] Metrics and observation

 