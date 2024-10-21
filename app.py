from api import api as app
from api.routes import api_blueprint

if __name__ == "__main__":
  app.register_blueprint(api_blueprint)
  app.run(debug=True)