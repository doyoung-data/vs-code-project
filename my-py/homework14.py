import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay

# 데이터 생성 (예시 데이터)
np.random.seed(42)
data = pd.DataFrame({
    'word_freq': np.random.randint(0, 20, 500),
    'email_length': np.random.randint(10, 500, 500),
    'domain_reputation': np.random.randint(1, 10, 500),
    'num_links': np.random.randint(0, 10, 500),
    'attachment_size': np.random.randint(0, 500, 500),
    'is_spam': np.random.choice([0, 1], size=500, p=[0.7, 0.3])
})

# 독립 변수와 종속 변수 설정
X = data[['word_freq', 'email_length', 'domain_reputation', 'num_links', 'attachment_size']]
y = data['is_spam']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 모델 1: 로지스틱 회귀
logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)
logistic_y_pred = logistic_model.predict(X_test)

# 모델 2: 랜덤 포레스트 분류
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
rf_y_pred = rf_model.predict(X_test)

# 평가 함수
def model_score(y_test, y_pred, model_name):
  print(f"\n{model_name} 평가:")
  print("Accuracy:", accuracy_score(y_test, y_pred))
  print("Precision:", precision_score(y_test, y_pred))
  print("Recall:", recall_score(y_test, y_pred))
  print("F1 Score:", f1_score(y_test, y_pred))
  print("confusion Matrix:", confusion_matrix(y_test, y_pred))

# 로지스틱 회귀 평가
model_score(y_test, logistic_y_pred, "Logistic Regression")

# 랜덤 포레스트 평가
model_score(y_test, rf_y_pred, "Random Forest")


# Precision-Recall Curve
PrecisionRecallDisplay.from_estimator(logistic_model, X_test, y_test)
plt.title("Precision-Recall Curve (Logistic Regression)")
plt.show()


PrecisionRecallDisplay.from_estimator(rf_model, X_test, y_test)
plt.title("Precision-Recall Curve (Random Forest)")
plt.show()