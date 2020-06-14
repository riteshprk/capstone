### Cinemake Project

[Heroku Link](https://capstoneapps.herokuapp.com/)

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.


### Models:
 - Movies with attributes title and release date
 - Actors with attributes name, age and gender
### Endpoints:
 - GET /actors and /movies
 - DELETE /actors/ and /movies/
 - POST /actors and /movies and
 - PATCH /actors/ and /movies/
### Roles:
 - Casting Assistant
   - Can view actors and movies
 - Casting Director
   - All permissions a Casting Assistant has and…
   - Add or delete an actor from the database
   - Modify actors or movies
 - Executive Producer
   - All permissions a Casting Director has and…
   - Add or delete a movie from the database
### Tests:
 - One test for success behavior of each endpoint
 - One test for error behavior of each endpoint
 - At least two tests of RBAC for each role

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/capstone` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

- [Flask-migrate](https://flask-migrate.readthedocs.io/en/latest/#) Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.


## Running the server

From within the `capstone` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python app.py
```

## Endpoints illustration

Following is the list of all available endpoints. 

### GET '/movies'
- Returns: Key, value pair of movies in which the keys are the id, title and release_date.
- Request Arguments: None
``` 
{
    "movies": [
        {
            "id": 1,
            "release_date": "Sun, 28 Jun 2020 00:00:00 GMT",
            "title": "dragons action"
        },
        {
            "id": 2,
            "release_date": "Wed, 22 Jul 2020 00:00:00 GMT",
            "title": "dive deep"
        },
        {
            "id": 3,
            "release_date": "Sat, 12 Sep 2020 00:00:00 GMT",
            "title": "house leader"
        },
        {
            "id": 4,
            "release_date": "Sun, 11 Oct 2020 00:00:00 GMT",
            "title": "captain murugan"
        },
        {
            "id": 5,
            "release_date": "Thu, 12 Nov 2020 00:00:00 GMT",
            "title": "The cycle of amusement"
        }
    ],
    "success": true
}
```

### GET '/actors'
- Returns: Key, value pair of actors in which the keys are the id, name, gender and age.
- Request Arguments: None

```
{
    "actors": [
        {
            "age": "39",
            "gender": "male",
            "id": 1,
            "name": "jack taylor5"
        },
        {
            "age": "39",
            "gender": "male",
            "id": 2,
            "name": "jack taylor"
        },
        {
            "age": "30",
            "gender": "female",
            "id": 3,
            "name": "angela faylor"
        },
        {
            "age": "35",
            "gender": "female",
            "id": 4,
            "name": "andrea taylor"
        },
        {
            "age": "38",
            "gender": "female",
            "id": 5,
            "name": "kangna ranaut"
        }
    ],
    "success": true
}

```
### GET '/movies/id/actors'
- Returns: It returns the key, value pair of actors playing in the given movie id. It also return the key, value pair of the given movie id . 
- Request Arguments: movie id
```
{
    "actors": [
        {
            "age": "39",
            "gender": "male",
            "id": 2,
            "name": "jack taylor"
        },
        {
            "age": "30",
            "gender": "female",
            "id": 3,
            "name": "angela faylor"
        }
    ],
    "movie": {
        "id": 2,
        "release_date": "Wed, 22 Jul 2020 00:00:00 GMT",
        "title": "dive deep"
    },
    "success": true
}

```
### PATCH '/movies/id/actors'
- Returns: It returns the updated key, value pair of actors playing in the given movie id. It also return the key, value pair of the given movie id . 
- Request Arguments: movie id, json body object containing actors id list as:
```
{
  actors: [1, 2]
}
```
response:
```
{
  "Question deleted": {
    "answer": "Brazil",
    "category": 6,
    "difficulty": 3,
    "id": 10,
    "question": "Which is the only team to play in every soccer World Cup tournament?"
  },
  "Total Question": 16,
  "success": true
}

```
### POST '/movies'
- Add new dictionary of movies key/value pairs in database.
- Request Arguments: json body object containing movies key/value pairs as shown below:
```
{
  "title": "captain murugan",
  "release_date": "2020-10-11"
}
```
- Returns: Newly added dictionary objects of movies containing keys/value pairs for id, title, release_date.

```
{
    "movies": {
      "id": 4,
      "release_date": "Sun, 11 Oct 2020 00:00:00 GMT",
      "title": "captain murugan"
    },
    "success": true
}
```
### POST '/actors'
- Add new dictionary of actor key/value pairs in database.
- Request Arguments: json body object containing actor key/value pairs as shown below:
```
{
  "name": "jack taylor",         
  "age": "39",         
  "gender": "male"         
}
```
- Returns: Newly added dictionary objects of actor containing keys/value pairs for id, name, age and gender.

```
{
    "actor": {
        "age": "39",
        "gender": "male",
        "id": 2,
        "name": "jack taylor"
    },
    "success": true
}
```
### PATCH '/movies/id'
- Modify dictionary of movies value in database.
- Request Arguments: movie id and json body object containing  movies key/value pairs whose modification is required either one key value pair or both.
```
{
    "release_date": "2020-10-22"
}
```
- Returns: Newly modified dictionary objects of movies containing keys/value pairs for id, title, release_date.

```
{
    "movies": {
      "id": 4,
      "release_date": "Thu, 22 Oct 2020 00:00:00 GMT",
      "title": "captain murugan"
    },
    "success": true
}
```
### PATCH '/actors/id'
- Modify dictionary of actor value in database.
- Request Arguments: actor id and json body object containing  movies key/value pairs whose modification is required either one key value pair or all.
```
{
    "name": "mark james"
}
```
- Returns: Newly modified dictionary objects of actor containing keys/value pairs for id, name, age, andd gender.

```
{
    "actor": {
        "age": "39",
        "gender": "male",
        "id": 1,
        "name": "mark james"
    },
    "success": true
}
```
## HTTP Errors response.

In the event of HTTP fetch error. Following is the list of response object.

|HTTP Error       	|Response Body                          											   |
|-------------------|--------------------------------------------------------------------------------------|
|400 Errors 		|{"error": 400, "success": false "message": "Bad request"}                             |
|404 Errors 		|{"error": 404, "success": false "message": "Not found"}                               |
|405 Errors 		|{"error": 405, "success": false "message": "Method not allowed"}				       |
|422 Errors 		|{"error": 422, "success": false "message": "Unprocessable"}					       |

## Testing
A seprate databse is configured in heroku to do the test. The sperate DATABASE_URL is provided in .env file.
There are total 10 Test which includes role base access test and authorisation error handling.
Please run the following script.
To run locally 
```
python test_app.py 
```
To run on heroku 
```
heroku run python test_app.py --app capstoneapps
```
Please use the following heroku link to check all above enpoints

[Heroku Link](https://capstoneapps.herokuapp.com/)
