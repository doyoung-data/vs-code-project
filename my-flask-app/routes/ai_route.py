from flask import render_template, request, jsonify, Blueprint

import joblib
import numpy as np

ai_route = Blueprint('ai', __name__)

# 모델 로드
lin_reg = joblib.load('house_price_model-lin.pkl')
rf_reg = joblib.load('house_price_model-rf.pkl')


# 예측 경로
@ai_route.route("/predict-house-price", methods=['GET'])
def predictHousePrice():
    # GET 요청에서 파라미터 추출
    area = request.args.get('area')
    rooms = request.args.get('rooms')
    year_built = request.args.get('year')
    income = request.args.get('income')
    school_rating = request.args.get('school_rating')
    transit_score = request.args.get('transit_score')

    # 특성 배열 생성
    features = np.array([[int(area), int(rooms), int(year_built),
                           int(income), int(school_rating), int(transit_score)]])

    # 예측 수행
    lin_reg_pred = lin_reg.predict(features)[0]
    rf_reg_pred = rf_reg.predict(features)[0]

    # 예측 결과를 JSON 형식으로 반환
    return jsonify({
        "message": "ok",
        "price_by_lin": lin_reg_pred,
        "price_by_rf": rf_reg_pred
    })
