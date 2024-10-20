from api import api
from api.routes import api_blueprint


api.register_blueprint(api_blueprint)
api.run(debug=True)