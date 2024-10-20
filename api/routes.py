from api import api
from api.services import add, minus, multiply, divide
from flask import Blueprint ,request, jsonify, render_template, redirect

api_blueprint = Blueprint('api', __name__)



@api_blueprint.route('/<path:path>')
def catch_all(path):
    return redirect('/')

@api_blueprint.route('/')
def index():
    return render_template('index.html')

@api_blueprint.route('/add/<int:a>/<int:b>', methods=['GET'])
def add_route(a, b):
    try:
        return jsonify({'status':200, 'result':add(a, b)})
    except Exception as e:
        return jsonify({'status':400, 'message':'Invalid URL'})

@api_blueprint.route('/minus/<int:a>/<int:b>', methods=['GET'])
def minus_route(a, b):
    try:
        return jsonify({'status':200, 'result':minus(a, b)})
    except Exception as e:
        return jsonify({'status':400, 'message':'Invalid URL'})

@api_blueprint.route('/multiply/<int:a>/<int:b>', methods=['GET'])
def multiply_route(a, b):
    try:
        return jsonify({'status':200, 'result':multiply(a, b)})
    except Exception as e:
        return jsonify({'status':400, 'message':'Invalid URL'})

@api_blueprint.route('/divide/<int:a>/<int:b>', methods=['GET'])
def divide_route(a, b):
    try:
        return jsonify({'status':200, 'result':divide(a, b)})
    except Exception as e:
        return jsonify({'status':400, 'message':'Invalid URL'})
