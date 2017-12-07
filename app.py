from flask import flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
from models import db

# Creates the basic Flask app
app = Flask(__name__)
# Initializes the app to use the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI 
# Hide the weird Flask warning messages
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Initialize the database created in models in the app's context
with app.app_context(): 
    db.init_app(app)
    db.create_all()


# Basic Flask route
@app.route('/')
def index():
	return "index"

# Runs the app (in debug mode)
if __name__ == "__main__":
    app.run(debug=True)
