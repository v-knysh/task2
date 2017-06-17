import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or "postgresql://knyshv:38kv1444@localhost/names_evo_summer_test_db"
db = SQLAlchemy(app)

from app import views, models
