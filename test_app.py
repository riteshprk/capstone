import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
#from flask import request, _request_ctx_stack, abort

from app import create_app
from models import setup_db, Movie, Actor, relation
from auth import get_token_auth_header, check_permissions, verify_decode_jwt


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}@{}/{}".format(
            'postgres:temp101', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_movie = {
            "title": "Dragon Den",
            "release_date": "20-07-2020"
        }

        self.new_actor = {
            "name": "Jack Taylor",
            "age": 35,
            "gender": "Male"
        }

        # self.movie_actors = {
        #     "actors": [1, 2]
        # }

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # def test_login_request(self):
    #     # credentials = {“username”:”un”, “password”:”pass”}
    #     headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVIMFEwOXJDU1phV1djYWpmdU52RCJ9.eyJpc3MiOiJodHRwczovL2Rldi1rYWpiZ2trNS5ldS5hdXRoMC5jb20vIiwic3ViIjoia1ZCUmR3S2JtdTMydTkxeWJ2VWs1S2w1dGpuU2ZLU2JAY2xpZW50cyIsImF1ZCI6Imh0dHA6Ly8xMjcuMC4wLjE6NTAwMCIsImlhdCI6MTU5MTg4NjMyNCwiZXhwIjoxNTkxOTcyNzI0LCJhenAiOiJrVkJSZHdLYm11MzJ1OTF5YnZVazVLbDV0am5TZktTYiIsInNjb3BlIjoiZ2V0Om1vdmllcyBwb3N0Om1vdmllcyBwYXRjaDptb3ZpZXMgZGVsZXRlOm1vdmllcyBnZXQ6YWN0b3JzIHBvc3Q6YWN0b3JzIHBhdGNoOmFjdG9ycyBkZWxldGU6YWN0b3JzIGdldDptb3ZpZXNfYWN0b3JzIHBhdGNoOm1vdmllc19hY3RvcnMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6bW92aWVzIiwicG9zdDptb3ZpZXMiLCJwYXRjaDptb3ZpZXMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsInBvc3Q6YWN0b3JzIiwicGF0Y2g6YWN0b3JzIiwiZGVsZXRlOmFjdG9ycyIsImdldDptb3ZpZXNfYWN0b3JzIiwicGF0Y2g6bW92aWVzX2FjdG9ycyJdfQ.JL_3JXjk0gRbJGZWD3VKEWOFiXoAsLC7r3ADP9FhP_Uaxlog61-NZzjhGQFVvKks7oSEmWVCzHntvXcyasfQtEHIFDLcBoKSW409iyfdupiAlczvX_TuLuxd6KGgSJkoEUAnLx6G5p69Ng1oZPXWzmcD-x9NmTrG5K5E6nC57H-b0hped7x8RqA10EF0sXTdTtrK2xPzdvX8QO4PAS9RdhGwJqiSKvrcLs65g22lynMf9fq6pd-ZsjYKu_gwTrt9JFcEf3MBzH3leDmVTjhdUXqYpumU60AJ-DsIxkpqlniQI4TKQ8m1DZ8gkQYI31ULhB_-KE31Qzq9d3AiUUdtWg'}
    #     resp = requests.get('http://localhost:5000/movies', headers=headers)
    #     # print(resp)
    #     data = (resp.__dict__)
    #     print(data)
    #     self.assertEqual(resp.status_code, 200)
    #self.assertEqual(resp.success, true)

    def test_get_movies(self):
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVIMFEwOXJDU1phV1djYWpmdU52RCJ9.eyJpc3MiOiJodHRwczovL2Rldi1rYWpiZ2trNS5ldS5hdXRoMC5jb20vIiwic3ViIjoia1ZCUmR3S2JtdTMydTkxeWJ2VWs1S2w1dGpuU2ZLU2JAY2xpZW50cyIsImF1ZCI6Imh0dHA6Ly8xMjcuMC4wLjE6NTAwMCIsImlhdCI6MTU5MTg4NjMyNCwiZXhwIjoxNTkxOTcyNzI0LCJhenAiOiJrVkJSZHdLYm11MzJ1OTF5YnZVazVLbDV0am5TZktTYiIsInNjb3BlIjoiZ2V0Om1vdmllcyBwb3N0Om1vdmllcyBwYXRjaDptb3ZpZXMgZGVsZXRlOm1vdmllcyBnZXQ6YWN0b3JzIHBvc3Q6YWN0b3JzIHBhdGNoOmFjdG9ycyBkZWxldGU6YWN0b3JzIGdldDptb3ZpZXNfYWN0b3JzIHBhdGNoOm1vdmllc19hY3RvcnMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6bW92aWVzIiwicG9zdDptb3ZpZXMiLCJwYXRjaDptb3ZpZXMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsInBvc3Q6YWN0b3JzIiwicGF0Y2g6YWN0b3JzIiwiZGVsZXRlOmFjdG9ycyIsImdldDptb3ZpZXNfYWN0b3JzIiwicGF0Y2g6bW92aWVzX2FjdG9ycyJdfQ.JL_3JXjk0gRbJGZWD3VKEWOFiXoAsLC7r3ADP9FhP_Uaxlog61-NZzjhGQFVvKks7oSEmWVCzHntvXcyasfQtEHIFDLcBoKSW409iyfdupiAlczvX_TuLuxd6KGgSJkoEUAnLx6G5p69Ng1oZPXWzmcD-x9NmTrG5K5E6nC57H-b0hped7x8RqA10EF0sXTdTtrK2xPzdvX8QO4PAS9RdhGwJqiSKvrcLs65g22lynMf9fq6pd-ZsjYKu_gwTrt9JFcEf3MBzH3leDmVTjhdUXqYpumU60AJ-DsIxkpqlniQI4TKQ8m1DZ8gkQYI31ULhB_-KE31Qzq9d3AiUUdtWg'}
        res = self.client().get('/movies', headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_405_error_get_movies(self):
        res = self.client().get('/movies/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Method not allowed")

    def test_404_error_get_paginated_questions(self):
        res = self.client().get('/adsatete')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not found")

    # def test_get_all_categories(self):
    #     res = self.client().get('/categories')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_categories'])
    #     self.assertTrue(len(data['categories']))

    # def test_404_error_get_all_categories(self):
    #     res = self.client().get('/categories/wqrwtwe')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], "Not found")

    # def test_delete_questions(self):
    #     res = self.client().delete('/questions/11')
    #     data = json.loads(res.data)

    #     if res.status_code == 200:
    #         self.assertEqual(res.status_code, 200)
    #         self.assertEqual(data['success'], True)
    #     else:
    #         self.assertEqual(res.status_code, 422)
    #         self.assertEqual(data['success'], False)

    # def test_422_error_delete_questions(self):
    #     res = self.client().delete('/questions/99999')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)

    # def test_404_error_delete_questions(self):
    #     res = self.client().delete('/questions/qeeqe')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)

    # def test_create_questions(self):
    #     res = self.client().post('/questions', json=self.new_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total questions'])
    #     self.assertTrue(len(data['questions']))

    # def test_405_error_create_questions(self):
    #     res = self.client().post('/questions/10', json=self.new_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 405)
    #     self.assertEqual(data['success'], False)

    # def test_search_question(self):
    #     res = self.client().post('/search', json=self.search_data)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)

    # def test_404_error_search_question(self):
    #     res = self.client().post('/search/233', json=self.search_data)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)

    # def test_quizzes(self):
    #     res = self.client().post('/quizzes', json=self.quizzes_data)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)

    # def test_422_error_quizzes(self):
    #     res = self.client().post('/quizzes', json=self.search_data)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)

    # def test_404_error_quizzes(self):
    #     res = self.client().post('/quizzes/1', json=self.search_data)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
