
## Xeneta Rates Test API
This project is based on the [test repository](https://github.com/xeneta/ratestask) related to rates task. It uses Python, FastAPI, and PostgreSQL built on Docker and Docker Compose.


### Running the project
_Use the following commands_

1. Clone the repo
   - _using ssh_
   ```sh
   git clone git@github.com:imay-dev/xeneta-rates.git
   ```
   - or _using https_
   ```sh
   git clone https://github.com/imay-dev/xeneta-rates.git
   ```
2. Build and Run the project
   ```sh
   docker-compose up -d
   ```
* Obviously the `docker-compose.yml` file runs a `postgresql` image and a `python` one to handle the app and imports `rates.sql` into `postgres` database. You can change the names clearly.  

* The app will run on `8080` using `uvicorn`. It has been set in `Dockerfile` and the port is mounted in `docker-compose.yml`.

### Running the tests
```sh
docker exec -i rates_app pytest
```

* You can simply run `pytest` command inside the `rates_app` container if you need to see the colored results of the tests.

### API Docs
The following links will lead you through built-in API Docs:
* [OpenAPI](http://localhost:8080/docs)
* [ReDoc](http://localhost:8080/redoc)