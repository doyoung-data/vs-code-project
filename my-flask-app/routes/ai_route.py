from flask import render_template,request,jsonify,Blueprint
import pymysql
from db import get_db_connection
import joblib
import pandas as pd 
import numpy as np

ai_route = Blueprint('ai',__name__)


lin_reg = joblib.load('house_price_model-lin.pkl')
rf_reg = joblib.load('house_price_model-rf.pkl')   

# 추가
@ai_route.route("/add-house", methods=["post"])
def addHouse():
    data = request.json

    area = data.get("area")
    year_built = data.get("year")
    income = data.get("income")
    school_rating = data.get("school_rating")
    transit_score = data.get("transit_score")
    rooms = data.get("rooms")
    pred_lin = data.get("pred_lin")
    pred_rf = data.get("pred_rf")

    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
        INSERT INTO house 
        (area, year_built, income, school_rating, transit_score, rooms, pred_lin, pred_rf, create_date) 
        VALUES 
        (%s, %s, %s, %s, %s, %s, %s, %s, sysdate())
    """
    # year_built로 변경된 변수 사용
    cursor.execute(query, (area, year_built, income, school_rating, transit_score, rooms, pred_lin, pred_rf))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "ok"})


@ai_route.route("/predict-house-price",methods=['get'])
def predictHousePrice():
    

    area = request.args.get('area')
    rooms = request.args.get('rooms')
    year_built = request.args.get('year')
    income = request.args.get('income')
    school_rating = request.args.get('school_rating')
    transit_score = request.args.get('transit_score')

    features = np.array([[
        int(area),
        int(rooms),
        int(year_built),
        int(income),
        int(school_rating),
        int(transit_score)
    ]])

    lin_reg_pred = lin_reg.predict(features)[0]
    rf_reg_pred = rf_reg.predict(features)[0]



    return jsonify({
        "message":"ok",
        "price_by_lin":lin_reg_pred,
        "price_by_rf":rf_reg_pred
        })
