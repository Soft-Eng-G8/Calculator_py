from api import api as app
from api.routes import api_blueprint

app.register_blueprint(api_blueprint)
# api.run(debug=True)