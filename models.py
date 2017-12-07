from flask_sqlalchemy import SQLAlchemy

# Database that is used throughout the app
# It is defined here to prevent circular imports
db = SQLAlchemy()