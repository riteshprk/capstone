import os
from flask import Flask, request, jsonify, abort, render_template
from sqlalchemy import exc
import json
from flask_cors import CORS


from models import setup_db, Actor, Movie, relation
from auth import AuthError, requires_auth


def create_app():
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

# ROUTES
    @APP.route('/', methods=['POST', 'GET'])
    def health():
        return jsonify("Healthy")

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors():
        try:
            actors = list(map(Actor.format, Actor.query.all()))
        except:
            abort(400)
        return jsonify({
            "success": True,
            "actors": actors
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actors():
        try:
            body = request.get_json()
            actor = Actor(name=body["name"],
                          age=body["age"], gender=body["gender"])
            actor.insert()
        except Exception as er:
            print(er)
            abort(400)
        return jsonify({
            "success": True,
            "actor": actor.format()
        })

    @app.route('/actors/<id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actors(id):
        try:
            body = request.get_json()
            print(body)
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            for key, value in body.items():
                setattr(actor, key, value)
            actor.update()
        except Exception as er:
            print(er)
            if actor is None:
                abort(404)
            abort(400)
        return jsonify({
            "success": True,
            "actor": actor.format()
        })

    @app.route('/actors/<id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(id):
        try:
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            actor.delete()
        except:
            if actor is None:
                abort(404)
            abort(400)
        return jsonify({
            "success": True,
            "delete": id
        })

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies():
        try:
            movies = list(map(Movie.format, Movie.query.all()))
        except:
            abort(400)
        return jsonify({
            "success": True,
            "movies": movies
        })

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movies():
        try:
            body = request.get_json()
            movie = Movie(
                title=body["title"], release_date=body["release_date"])
            movie.insert()
        except Exception as er:
            print(er)
            abort(400)
        return jsonify({
            "success": True,
            "movies": movie.format()
        })

    @app.route('/movies/<id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movies(id):
        try:
            body = request.get_json()
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            for key, value in body.items():
                setattr(movie, key, value)
            movie.update()
        except:
            if movie is None:
                abort(404)
            abort(400)
        return jsonify({
            "success": True,
            "drinks": movie.format()
        })

    @app.route('/movies/<id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(id):
        try:
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            movie.delete()
        except:
            if movie is None:
                abort(404)
            abort(400)
        return jsonify({
            "success": True,
            "delete": id
        })

    @app.route('/movies/<id>/actors', methods=['GET'])
    @requires_auth('get:movies_actors')
    def get_movie_actors(id):
        try:
            movie = Movie.query.filter(Movie.id == id).one_or_none()
        except:
            if movie is None:
                abort(404)
            abort(400)
        return jsonify({
            "success": True,
            "movie": movie.format(),
            "actors": [actor.format() for actor in movie.actors]
        })

    @app.route('/movies/<id>/actors', methods=['PATCH'])
    @requires_auth('patch:movies_actors')
    def update_movie_actors(id):
        try:
            body = request.get_json()
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            actors = body['actors']
            movie.actors.clear()
            for actor in actors:
                actor_list = Actor.query.filter(
                    Actor.id == actor).one_or_none()
                movie.actors.append(actor_list)
                movie.update()
        except:
            if movie is None:
                abort(404)
            abort(400)
        return jsonify({
            "success": True,
            "movie": movie.format(),
            "actors": [actor.format() for actor in movie.actors]
        })

    # Error Handling

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request",
        }), 400

    @app.errorhandler(401)
    def unauthorize_request(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized request",
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found",
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed",
        }), 405

    @ app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


# # Error handler

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
