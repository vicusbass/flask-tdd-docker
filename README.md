# flask-tdd-docker
Trying out a microservice with Flask.

Build it:

`docker-compose build`

Run it:

`docker-compose up -d`

Update it:

`docker-compose up -d --build`

Run tests:

`docker-compose exec users python -m pytest "project/tests"`

