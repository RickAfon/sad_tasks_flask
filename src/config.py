import os
from dotenv import load_dotenv
from app import app
from uuid import uuid4
from flask_wtf.csrf import CSRFProtect

load_dotenv()

app.secret_key = str(uuid4())
csrf = CSRFProtect(app)

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")

SQLALCHEMY_TRACK_MODIFICATIONS = True