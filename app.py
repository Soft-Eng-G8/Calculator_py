from api import api
from api.routes import api_blueprint

if __name__ == "__main__":
  api.register_blueprint(api_blueprint)
  api.run(debug=True)