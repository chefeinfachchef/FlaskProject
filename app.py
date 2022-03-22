from flask import Flask
from models.models import db
from flask.templating import render_template
from controllers.blueprint import Reise_blueprint
from controllers.index_blueprint import index_blueprint

import sqlalchemy
app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Reise"

db.init_app(app)

# blueprint registrierung 
app.register_blueprint(index_blueprint)
app.register_blueprint(Reise_blueprint)

app.run(debug=True)

