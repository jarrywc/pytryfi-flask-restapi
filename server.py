import pytryfi

import requests
import flask
import os
import flask_login
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
import json
from urllib.parse import quote_plus
#from flask_oauthlib.client import OAuth, OAuthException
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv(find_dotenv())
username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")

tryfi = pytryfi.PyTryFi(username, password)
print(tryfi)
tryfi.pets[0].updateStats(tryfi.session)

getAddr = tryfi.pets[0].getCurrPlaceAddress()
getSteps = tryfi.pets[0].getDailySteps()
getActivity = tryfi.pets[0].getActivityType()

print(f'Address {getAddr}')
print(f'Steps {getSteps}')
print(f'Activity {getActivity}')