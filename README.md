# 🏠 HBnB Evolution

Welcome to the HBnB Evolution project. This project is a web application inspired by Airbnb, developed in Python using the Flask framework. This repository contains the backend API source code, including the management of users, places, amenities, reviews, countries, and cities.

## Table of Contents

- [Description 📖](#description)
- [Project Structure 📂](#project-structure)
- [Models 🌟](#models)
- [Endpoints 🔥](#endpoints)
- [Prerequisites 📝](#prerequisites)
- [Installation 💿](#installation)
- [Docker 🐋](#docker)
- [Tests ✅](#tests)
- [UML Diagram 🗺️](#uml-diagram)
- [Authors 🧪](#authors)

<a name="description"></a>
## Description 📖

The HBnB Evolution API allows managing entities such as users, places, amenities, reviews, countries, and cities. It provides RESTful endpoints to create, read, update, and delete these entities. The API is built using Flask and Flask-RESTx for easy endpoint documentation and manipulation.

<a name="project-structure"></a>
## Project Structure 📂

- **api/** : Contains the routes and controllers for the different models.
- **model/** : Contains the data models representing the entities.
- **persistence/** : Contains the persistence classes for managing CRUD operations.
- **data_manager.py** : Manages CRUD operations across different entity types.
- **Dockerfile** : For containerizing the application with Docker.
- **requirements.txt** : List of Python dependencies.

<a name="models"></a>
## Models 🌟

- **User** : Represents a user of the application.
- **Place** : Represents a place available for rent.
- **Review** : Represents a review of a place.
- **Amenity** : Represents an amenity available in a place.
- **City** : Represents a city where places are located.
- **Country** : Represents a country that contains cities.

<a name="endpoints"></a>
## Endpoints 🔥

### User

- **POST /users** : Create a new user.
- **GET /users** : Retrieve all users.
- **GET /users/{user_id}** : Retrieve a user by their ID.
- **PUT /users/{user_id}** : Update an existing user.
- **DELETE /users/{user_id}** : Delete a user.

### Place

- **POST /places** : Create a new place.
- **GET /places** : Retrieve all places.
- **GET /places/{place_id}** : Retrieve a place by its ID.
- **PUT /places/{place_id}** : Update an existing place.
- **DELETE /places/{place_id}** : Delete a place.

### Review

- **POST /places/{place_id}/reviews** : Create a new review for a place.
- **GET /users/{user_id}/reviews** : Retrieve all reviews written by a user.
- **GET /places/{place_id}/reviews** : Retrieve all reviews for a place.
- **GET /reviews/{review_id}** : Retrieve a review by its ID.
- **PUT /reviews/{review_id}** : Update an existing review.
- **DELETE /reviews/{review_id}** : Delete a review.

### Amenity

- **POST /amenities** : Create a new amenity.
- **GET /amenities** : Retrieve all amenities.
- **GET /amenities/{amenity_id}** : Retrieve an amenity by its ID.
- **PUT /amenities/{amenity_id}** : Update an existing amenity.
- **DELETE /amenities/{amenity_id}** : Delete an amenity.

### City

- **POST /cities** : Create a new city.
- **GET /cities** : Retrieve all cities.
- **GET /cities/{city_id}** : Retrieve a city by its ID.
- **PUT /cities/{city_id}** : Update an existing city.
- **DELETE /cities/{city_id}** : Delete a city.

### Country

- **GET /countries** : Retrieve all countries.
- **GET /countries/{country_code}** : Retrieve a country by its code.
- **GET /countries/{country_code}/cities** : Retrieve all cities in a country.

<a name="prerequisites"></a>
## Prerequisites 📝

Before starting, ensure you have the following installed on your machine:

- Python 3.8+
- pip (Python package installer)
- Docker (optional, for containerization)

<a name="installation"></a>
## Installation 💿

Clone this repository to your local machine:

```sh
git clone https://github.com/Ho2bes/holbertonschool-hbnb/

cd holbertonschool-hbnb
```

If you're not using Docker:

- Install the required Python dependencies:

  ```sh
  pip install -r requirements.txt
  ```

- To start the Flask server locally, run the following command:

  ```sh
  python3 main.py
  ```

  The server will be accessible at [`http://127.0.0.1:5001/`](http://127.0.0.1:5001/).

<a name="docker"></a>
## Docker 🐋

To containerize the application with Docker:

1. Build the Docker image:

   ```sh
   docker build -t holbertonschool-hbnb .
   ```

2. Run the Docker container:

   ```sh
   docker run -d -p 8001:8000 -v $(pwd)/data:/app/data --name hbnb_container -e PORT=8000 holbertonschool-hbnb
   ```

3. Click on this link:
   ## [🏡 Best Hbnb site in the world !!](http://localhost:8001/)

<a name="tests"></a>
## Tests ✅

To run the unit tests, use the following command:

```sh
python3 -m unittest discover -s tests
```

<a name="uml-diagram"></a>
## UML Diagram 🗺️

![UML Diagram](./uml_diagram.png)

<a name="authors"></a>
## Authors 🧪

- [N. B. Domingo](https://github.com/Ho2bes/)
- [Francia Ramarolahy](https://github.com/Francianeny/)
- [Tifenn Guérin](https://github.com/GuerinTifenn/)

---

This project is developed as part of the Holberton School curriculum. For more information, please visit [Holberton School](https://www.holbertonschool.com).
