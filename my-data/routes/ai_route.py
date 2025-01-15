from flask import render_template,request,jsonify,Blueprint
import pandas as pd 
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os

ai_route = Blueprint('ai',__name__)


# 모델 로드
model = tf.keras.models.load_model('C:/Users/do543/vs-code-project/vs-code-project/my-data/mobilenet_cats_and_dogs_classifier.h5')

# 이미지 전처리 함수
def load_and_preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))  # 모델에 맞는 크기로 조정
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # 배치 추가
    img_array = img_array / 255.0  # 스케일 조정
    return img_array

@ai_route.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    # 이미지 파일 저장
    image_file = request.files['image']
    file_path = os.path.join("uploads", image_file.filename)
    os.makedirs("uploads", exist_ok=True)
    image_file.save(file_path)

    # 이미지 전처리 및 예측
    try:
        preprocessed_img = load_and_preprocess_image(file_path)
        prediction = model.predict(preprocessed_img)

        # 결과 반환
        if prediction[0] > 0.5:
            result = {
                "label": "Dog",
                "confidence": float(prediction[0][0])
            }
        else:
            result = {
                "label": "Cat",
                "confidence": float(1 - prediction[0][0])
            }

        # 처리 후 임시 파일 삭제
        os.remove(file_path)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    ai_route.run(debug=True)