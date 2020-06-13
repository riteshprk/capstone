### Capstone Project
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

## Endpoints examples

Following is the list of all available endpoints. 

### GET '/movies'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, movies, that contains a object of id: movie_string key:value pairs.
``` 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}
```

### GET '/questions'
- Fetches a dictionary of question in which the keys are the id, question, answer, category and difficulty and their corresponding value are returned. This also fetches the dictionary of categories as explained above.
- Request Arguments: None
- Returns: All dictionary objects of question containing keys/value pairs for id, question, answer, category, difficulty. It will also return total question count and current category value.

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,

  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her be
loved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man w
ith multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"

    }
  ],
  "success": true,
  "total_questions": 17
}

```
### GET '/categories/id/questions'
- Fetches a dictionary of question for given category id.
- Request Arguments: id. Example: /categories/2/questions. To fetch questions for category 2.
- Returns: All dictionary objects of question containing keys/value pairs for id, question, answer, category, difficulty. It will also return total question count for the given category and current category value.

```
{
  "current_category": 2,
  "questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"

    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading expo
nent of action painting?"
    }
  ],
  "success": true,
  "total_questions": 4
}

```
### DELETE '/questions/id'
- Deletes a question record from the database for given category id.
- Request Arguments: id. Example: /questions/10. To delete question record whose id is 10.
- Returns: The deleted question dictionary key/value pairs. It also returns total question count in the database.

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
### POST '/questions'
- Add new dictionary of question key/value pairs in database.
- Request Arguments: json body object containing question, answer, category and difficulty as key parameters with coresponding values.
- Returns: All dictionary objects of questions containing keys/value pairs for id, question, answer, category, difficulty. It also returns added question id and total question count value.
```
{
  "created": 111,
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her be
loved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man w
ith multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"

    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    }
  ],
  "success": true,
  "total questions": 17
}
```
### POST '/search'
- Fetch dictionary of questions whose question value contains search term.
- Request Arguments: json body object containing "searchTerm" key/value pairs.
- Returns: Dictionary objects of questions containing keys/value pairs for id, question, answer, category, difficulty where question value contains search term. It also returns total question count value. For example: "searchTerm":"body" return following result.
```
{
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    }
  ],
  "success": true,
  "total questions": 1
}
```
### POST '/quizzes'
- Fetch dictionary of question for selected category.
- Request Arguments: json body object containing quiz category id and type key/value pairs and previous questions list value. See the example below.
```
{"quiz_category":{"id":"1", "type":"science"}, "previous_questions":[]}
```
- Returns: Dictionary objects of question containing keys/value pairs for id, question, answer, category, difficulty.
```
{
  "question": {
    "answer": "98 %",
    "category": 1,
    "difficulty": 4,
    "id": 110,
    "question": "Humans and chimpanzees share roughly how much DNA?"
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
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```