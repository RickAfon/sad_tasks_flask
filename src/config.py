import os
from dotenv import load_dotenv
from app import app
from uuid import uuid4
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

load_dotenv()

app.secret_key = str(uuid4())
csrf = CSRFProtect(app)

Bcrypt(app)

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")

SQLALCHEMY_TRACK_MODIFICATIONS = True