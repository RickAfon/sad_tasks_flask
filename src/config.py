from app import app
from uuid import uuid4
from flask_wtf.csrf import CSRFProtect

app.secret_key = str(uuid4())
csrf = CSRFProtect(app)