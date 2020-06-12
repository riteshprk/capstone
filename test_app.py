import os
from dotenv import load_dotenv
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
# from flask import request, _request_ctx_stack, abort

from app import create_app
from models import setup_db, Movie, Actor, relation, db
from auth import get_token_auth_header, check_permissions, verify_decode_jwt

load_dotenv()
token = os.environ.get("api-token")
casting_assitant_token = os.environ.get("casting_assitant_token")
casting_director_token = os.environ.get("casting_director_token")
excutive_producer_token = os.environ.get("excutive_producer_token")


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}@{}/{}".format(
            'postgres:temp101', 'localhost:5432', self.database_name)

        # binds the app to the current context
        with self.app.app_context():
            self.db = db
            setup_db(self.app, self.database_path)
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_movie = {
            "title": "Dragon Den2",
            "release_date": "20-07-2020"
        }

        self.new_actor = {
            "name": "Jack Taylor",
            "age": 35,
            "gender": "Male"
        }

    def tearDown(self):
        """Executed after each test"""
        self.db.drop_all()

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_header_missing(self):
        headers = {}
        res = self.client().get('/movies', headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data, {
            'code': 'authorization_header_missing',
            'description': 'Authorization header is expected.'
        })

    def test_header_no_bearer(self):
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'afsafsg'}
        res = self.client().get('/movies', headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data, {
            'code': 'invalid_header',
            'description': "Authorization header must start with 'Bearer'."
        })

    def test_header_invalid_header(self):
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ewreewys'}
        res = self.client().get('/movies', headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data, {
            'code': 'invalid_header',
            'description': 'Unable to find appropriate token'
        })

    def test_405_error_get_movies(self):
        res = self.client().get('/movies/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Method not allowed")

    def test_404_error(self):
        res = self.client().get('/adsatete')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not found")

    '''
    Role based test
    '''

    def test_executive_producer_success(self):
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(excutive_producer_token)}
        res = self.client().post('/movies', headers=headers, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_casting_director_success(self):
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(casting_director_token)}
        res = self.client().post('/actors', headers=headers, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_casting_assitant_success(self):
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(casting_assitant_token)}
        res = self.client().get('/actors', headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_casting_assitant_permission_fail(self):
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(casting_assitant_token)}
        res = self.client().post('/actors', headers=headers, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data, {
            "code": "unauthorized",
            "description": "Permission not found."
        })

    def test_casting_director_permission_fail(self):
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(casting_director_token)}
        res = self.client().post('/movies', headers=headers, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data, {
            "code": "unauthorized",
            "description": "Permission not found."
        })

    # def test_casting_director_success(self):
    #     headers = {'Content-Type': 'application/json',
    #                'Authorization': 'Bearer {}'.format(casting_director_token)}
    #     res = self.client().delete('/actors/1', headers=headers)
    #     data = json.loads(res.data)
    #     if res.status_code == 200:
    #         self.assertEqual(res.status_code, 200)
    #         self.assertEqual(data['success'], True)
    #     else:
    #         self.assertEqual(res.status_code, 422)
    #         self.assertEqual(data['success'], False)

    # def test_casting_assitant_permission_fail(self):
    #     headers = {'Content-Type': 'application/json',
    #                'Authorization': 'Bearer {}'.format(casting_assitant_token)}
    #     res = self.client().post('/actors', headers=headers, json=self.new_actor)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 403)
    #     self.assertEqual(data, {
    #         "code": "unauthorized",
    #         "description": "Permission not found."
    #     })
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
