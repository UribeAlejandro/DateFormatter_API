# Date Formatter - API <!-- omit in toc -->

This is a simple API that returns today's date or current time. This is part of the interview process for the position of Machine Learning Engineer.

## Table of contents <!-- omit in toc -->

- [Requirements](#requirements)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
  - [Virtual Environment](#virtual-environment)
  - [Docker](#docker)
- [Testing](#testing)
- [References](#references)


## Requirements

> The second exercise consists of implementing an API in Python using FastAPI or in Golang that receives:
> - A POST request with a boolean parameter that responds with the current date in the format yyyy-mm-dd hh:ii:ss if the parameter is true, and returns the date in the format yyyy-dd-mm if the parameter is false.
> - A GET request that retrieves the value of a counter indicating how many times either of the two endpoints was called.

## Architecture

The API is built using FastAPI, a modern web framework for building APIs with Python. The API is containerized using Docker and docker-compose. The API is tested using Pytest.

The API has the following endpoints:

| Endpoint      | HTTP Method | Result                            |
| ------------- | ----------- | --------------------------------- |
| /             | GET         | Greeting message                  |
| /date         | POST        | Get the current date or timestamp |
| /date/counter | GET         | Get the                           |
| /health       | GET         | update a summary                  |

The route `date/` implements a [thread-safe Singleton](https://refactoring.guru/design-patterns/singleton) pattern to keep track of the number of times the endpoint was called. The counter is incremented every time the endpoint (`date/` *or* `data/counter`) is called.

## Installation

To install the API, you need to have Python 3.11 or higher installed on your machine. You can create a virtual environment by running the following command:

```bash
make venv
```

Then, install the required packages by running the following command:

```bash
make install
```

## Usage

### Virtual Environment

To start the API, run the following command:

```bash
make run-server
```

The API will be available at `http://localhost:8000`.

### Docker

You need `docker-compose` and `docker` installed. To build the Docker image, run the following command:

```bash
docker-compose build
```

To start the API using Docker, run the following command:

```bash
docker-compose up -d
```

The API will be available at `http://localhost:8000`.

To stop the API, run the following command:

```bash
docker-compose down -v
```

## Testing

To run the tests (on top of the virtualenv), run the following command:

```bash
make test
```

Or using Docker:

```bash
docker-compose exec api pytest tests/
```

## References

- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Pytest](https://docs.pytest.org/)
- [Refactoring Guru](https://refactoring.guru/)
