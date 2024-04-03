### Starter kit with:
1. FastAPI python framework
2. Nginx as the web server
3. Dockerised fastPI and the docker compose entire project
4. postgresSQL database in docker container
5. Alembic for database migrations
6. basic tests also included
---

**About:**

* The project is API to serve backend of Omnia webapp and safety app.
* Docker compose contain services for fleet_backend_v2, db and nginx
* nginx is used to facilitate `https` protocol
* certificate (.pem) files are configured to be kept in the root of the project

**How to start application**
step 1: clone the repo

step 2: Copy the .example.env file and make a copy as .env and fill in the actual values

step 3: Generate key.pem and cert.pem using following command in the root folder
`openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`

step 4: Run docker command (use development version for development)
`docker-compose -f docker-compose.dev.yaml up -d` (for development)
`docker-compose -f docker-compose.prod.yaml up -d` (for production)

This should start all docker services

API documentation is accessible on `/docs` e.g `https://localhost/docs`

##### To run locally

* Create a vitual env and activate it
```bash
python3 -m venv env_name
source env_name/bin/activate
```

* Install dependencies
```bash
pip3 install -r requirements.txt
```

* Start local server (with reload option)
```bash
uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
```

###### Database migrations
The migration command is to be run depending on where ther server is running, \
if its inside a docker container, migrations need to be run inside the container 

- Generate a migration command
`alembic revision --autogenerate -m "Initial migration"`

- Apply migrations: To apply the migrations to database, use command:
`alembic upgrade head`

---
