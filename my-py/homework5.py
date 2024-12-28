from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, r2_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# 데이터셋 로드
wine = load_wine()
X = wine.data
y = wine.target

# 데이터셋 나누기 (Train/Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# KNN 분류기 생성
knn = KNeighborsClassifier(n_neighbors=3)  # K=3
knn.fit(X_train, y_train)

# 예측
y_pred = knn.predict(X_test)

# 평가 결과 출력
print("=== KNN Evaluation ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
# R² 계산
r2 = r2_score(y_test, y_pred)
print("R² Score:", r2)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 혼동 행렬 출력
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=wine.target_names)
disp.plot(cmap="Blues")
plt.title("SVM - Confusion Matrix")
plt.show()