from flask import *
auth=Blueprint('auth',__name__)
from . import views,forms
