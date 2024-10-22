
# Calculator-Py
A simple calculator API using flask.
You can access this site/api from here: [calculator-py.app](https://calculator-py-phi.vercel.app/)

### Usage
<!-- TODO for Documenter -->

# Calculator-Py
A simple calculator API using flask.
You can access this site/api from here: [calculator-py.app](https://calculator-py-phi.vercel.app/)

## Features

- **Addition**: Add two numbers.
- **Subtraction**: Subtract one number from another.
- **Multiplication**: Multiply two numbers.
- **Division**: Divide one number by another, with error handling for division by zero.
- **Error Handling**: Returns appropriate error messages for invalid input or other errors.

## File: `routes.py`

This module defines the API routes for the calculator.

### Routes:

- **`/<path:path>` (GET):**
  - **Description**: Redirects any unmatched routes to the root URL (`/`).
  
- **`/` (GET):**
  - **Description**: Renders the `index.html` template (homepage).

- **`/add/<string:a>/<string:b>` (GET):**
  - **Description**: Adds two numbers (`a` and `b`) and returns the result in JSON format.
  - **Response**:
    - Success: `{ 'status': 200, 'result': <sum> }`
    - Error: `{ 'status': 400, 'message': 'Invalid input, please provide numbers' }`

- **`/minus/<string:a>/<string:b>` (GET):**
  - **Description**: Subtracts the second number (`b`) from the first number (`a`) and returns the result in JSON format.
  - **Response**:
    - Success: `{ 'status': 200, 'result': <difference> }`
    - Error: `{ 'status': 400, 'message': 'Invalid input, please provide numbers' }`

- **`/multiply/<string:a>/<string:b>` (GET):**
  - **Description**: Multiplies two numbers (`a` and `b`) and returns the result in JSON format.
  - **Response**:
    - Success: `{ 'status': 200, 'result': <product> }`
    - Error: `{ 'status': 400, 'message': 'Invalid input, please provide numbers' }`

- **`/divide/<string:a>/<string:b>` (GET):**
  - **Description**: Divides the first number (`a`) by the second number (`b`) and returns the result in JSON format. Handles division by zero errors.
  - **Response**:
    - Success: `{ 'status': 200, 'result': <quotient> }`
    - Error:
      - `{ 'status': 400, 'message': 'Invalid input, please provide numbers' }`
      - `{ 'status': 400, 'message': 'Division by zero is not allowed' }`

### Error Handling:

- Returns a 400 status code with an appropriate message for invalid input or any other errors.
- Returns a 400 status code with a specific message for division by zero errors.

---

## File: `services.py`

This module contains the logic for performing arithmetic operations.

### Functions:

- **`add(a: float, b: float) -> float`**
  - **Description**: Returns the sum of `a` and `b`.
  - **Returns**: The sum of `a` and `b`.

- **`minus(a: float, b: float) -> float`**
  - **Description**: Returns the difference when `b` is subtracted from `a`.
  - **Returns**: The difference between `a` and `b`.

- **`multiply(a: float, b: float) -> float`**
  - **Description**: Returns the product of `a` and `b`.
  - **Returns**: The product of `a` and `b`.

- **`divide(a: float, b: float) -> float`**
  - **Description**: Divides `a` by `b` and returns the result. Raises an error if `b` is zero.
  - **Returns**: The quotient of `a` divided by `b`.
  - **Raises**: `ValueError` if `b` is zero (division by zero is not allowed).

---

## File: `app.py`

This file sets up the Flask application and registers the API routes.

### Content:

- **`from api import api as app`**: Imports the `Flask` instance from `api`.
- **`from api.routes import api_blueprint`**: Imports the blueprint containing the defined routes from `routes.py`.
- **`app.register_blueprint(api_blueprint)`**: Registers the API blueprint with the Flask application.

### Purpose:

- This file ties together the main `Flask` app with the defined API routes in `routes.py` to expose the calculator's functionality via HTTP endpoints.

---

## File: `__init__.py`

This file initializes the Flask app.

### Content:

- **`from flask import Flask`**: Imports Flask to create a web application.
- **`api = Flask(__name__)`**: Initializes a Flask application instance.

### Purpose:

- This file sets up the base `Flask` application under the `api` variable, which is then used throughout the application to register routes and run the web server.

---

## Overall Flow

1. **`__init__.py`**: Creates the Flask application.
2. **`services.py`**: Defines the core logic for arithmetic operations.
3. **`routes.py`**: Defines the HTTP routes that trigger the services and return results in JSON.
4. **`app.py`**: Registers the routes with the main Flask app to make the API accessible.


### Build
Just go to `scripts` and launch `launch.bat/sh` depending on your system

### Build
Just go to `scripts` and launch `launch.bat/sh` depending on your system
