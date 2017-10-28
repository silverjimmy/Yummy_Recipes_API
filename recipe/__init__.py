from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "This is bruno"

from recipe import models
from recipe import views
