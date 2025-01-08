import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 데이터 생성 (예시 데이터)
np.random.seed(42)
data = pd.DataFrame({
    'area': np.random.randint(50, 200, 500),
    'rooms': np.random.randint(1, 6, 500),
    'year_built': np.random.randint(1980, 2021, 500),
    'income': np.random.randint(3000, 12000, 500),
    'school_rating': np.random.randint(1, 10, 500),
    'transit_score': np.random.randint(1, 10, 500),
    'price': np.random.randint(20000, 100000, 500)
})

# 독립 변수와 종속 변수 설정
X = data[['area', 'rooms', 'year_built', 'income', 'school_rating', 'transit_score']]
y = data['price']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 1: 선형 회귀
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_y_pred = linear_model.predict(X_test)

# 모델 2: 랜덤 포레스트 회귀 RandomForestRegression()
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)
rf_y_pred = rf_model.predict(X_test)

# 평가

# 선형 회귀 평가
linear_mse = mean_squared_error(y_test, linear_y_pred)
linear_r2 = r2_score(y_test, linear_y_pred)

# 랜덤 포레스트 평가
rf_mse = mean_squared_error(y_test, rf_y_pred)
rf_r2 = r2_score(y_test, rf_y_pred)

# 출력
print("선형 회귀 모델 평가:")
print(f"RMSE: {linear_mse:.2f}")
print(f"R²: {linear_r2:.2f}")

print("\n랜덤 포레스트 모델 평가:")
print(f"RMSE: {rf_mse:.2f}")
print(f"R²: {rf_r2:.2f}")