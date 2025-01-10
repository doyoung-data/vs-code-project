from flask import render_template,request,jsonify,Blueprint
import pymysql
from db import get_db_connection


user_route = Blueprint('user',__name__)

@user_route