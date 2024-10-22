from api import api

"""
This module defines the API routes for the Calculator application.
Routes:
    /<path:path> (GET): Redirects any unmatched routes to the root URL.
    / (GET): Renders the index.html template.
    /add/<string:a>/<string:b> (GET): Adds two numbers and returns the result in JSON format.
    /minus/<string:a>/<string:b> (GET): Subtracts the second number from the first and returns the result in JSON format.
    /multiply/<string:a>/<string:b> (GET): Multiplies two numbers and returns the result in JSON format.
    /divide/<string:a>/<string:b> (GET): Divides the first number by the second and returns the result in JSON format.
Error Handling:
    - Returns a 400 status code with an appropriate message for invalid input or other errors.
    - Returns a 400 status code with a message for division by zero errors.
"""
from api.services import add, minus, multiply, divide
from flask import Blueprint ,request, jsonify, render_template, redirect

api_blueprint = Blueprint('api', __name__)




@api_blueprint.route('/<path:path>')
def catch_all(path):
    return redirect('/')

@api_blueprint.route('/')
def index():
    return render_template('index.html')

@api_blueprint.route('/add/<string:a>/<string:b>', methods=['GET'])
def add_route(a, b):
    try:
        a = float(a)
        b = float(b)
        return jsonify({'status': 200, 'result': add(a, b)})
    except ValueError:
        return jsonify({'status': 400, 'message': 'Invalid input, please provide numbers'}), 400
    except Exception as e:
        return jsonify({'status': 400, 'message': 'An error occurred'}) , 400

@api_blueprint.route('/minus/<string:a>/<string:b>', methods=['GET'])
def minus_route(a, b):
    try:
        a = float(a)
        b = float(b)
        return jsonify({'status': 200, 'result': minus(a, b)})
    except ValueError:
        return jsonify({'status': 400, 'message': 'Invalid input, please provide numbers'}) , 400
    except Exception as e:
        return jsonify({'status': 400, 'message': 'An error occurred'}), 400

@api_blueprint.route('/multiply/<string:a>/<string:b>', methods=['GET'])
def multiply_route(a, b):
    try:
        a = float(a)
        b = float(b)
        return jsonify({'status': 200, 'result': multiply(a, b)})
    except ValueError:
        return jsonify({'status': 400, 'message': 'Invalid input, please provide numbers'}) , 400
    except Exception as e:
        return jsonify({'status': 400, 'message': 'An error occurred'}) , 400

@api_blueprint.route('/divide/<string:a>/<string:b>', methods=['GET'])
def divide_route(a, b):
    try:
        a = float(a)
        b = float(b)
        return jsonify({'status': 200, 'result': divide(a, b)}) 
    except ValueError:
        return jsonify({'status': 400, 'message': 'Invalid input, please provide numbers'}) , 400
    except ZeroDivisionError:
        return jsonify({'status': 400, 'message': 'Division by zero is not allowed'}) , 400
    except Exception as e:
        return jsonify({'status': 400, 'message': 'An error occurred'}) , 400
