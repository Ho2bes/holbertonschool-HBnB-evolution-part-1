# HBnB Evolution API

Welcome to the HBnB Evolution project. This project is a web application inspired by Airbnb, developed in Python using the Flask framework. This repository contains the backend API source code, including the management of users, places, amenities, reviews, countries, and cities.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [Documentation](#documentation)
- [Authors](#authors)

## Description

The HBnB Evolution API allows managing entities such as users, places, amenities, reviews, countries, and cities. It provides RESTful endpoints to create, read, update, and delete these entities. The API is built using Flask and Flask-RESTx for easy endpoint documentation and manipulation.

## Features

- **User Management**: Create, read, update, and delete users.
- **Place Management**: Create, read, update, and delete places.
- **Amenity Management**: Create, read, update, and delete amenities.
- **Review Management**: Create, read, update, and delete reviews.
- **Country and City Management**: Read pre-loaded countries and manage cities.
- **API Documentation**: Automatically generated via Flask-RESTx.

## Prerequisites

Before starting, ensure you have the following installed on your machine:

- Python 3.9+
- pip (Python package installer)
- Docker (optional, for containerization)

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/holbertonschool-HBnB-evolution-part-1.git
cd holbertonschool-HBnB-evolution-part-1
```

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Starting the Server

To start the Flask server locally, run the following command:

```bash
python3 app.py
```

The server will be accessible at `http://0.0.0.0:8000/`.

### Accessing the API Documentation

Once the server is running, you can access the automatically generated Swagger documentation at:

```bash
http://0.0.0.0:8000/swagger
```

### Using Docker

To run the application in a Docker container, follow these steps:

1. Build the Docker image:

```bash
docker build -t hbnb-evolution-api .
```

2. Run the Docker container:

```bash
docker run -p 8000:8000 hbnb-evolution-api
```

The server will be accessible at `http://0.0.0.0:8000/`.

## Tests

To run the unit tests, use the following command:

```bash
python3 -m unittest discover -s tests
```

Make sure all tests pass before deploying or modifying the code.

## Documentation

The API endpoints are documented via Flask-RESTx. You can access the complete documentation at the `/swagger` endpoint once the server is running.

## Authors

- [Nicolas Brault Domingo](https://github.com/Ho2bes/)
- [Francia Ramarolahy](https://github.com/Francianeny/)
- [Tifenn Guerin](https://github.com/GuerinTifenn/)

---

This project is developed as part of the Holberton School curriculum. For more information, please visit [Holberton School](https://www.holbertonschool.com).
