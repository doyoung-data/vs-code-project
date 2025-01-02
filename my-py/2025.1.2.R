# 1. ggplot2 패키지 설치
install.packages("ggplot2")

# 2. ggplot2 패키지 로드
library(ggplot2)

# 3. ggplot2 내장 데이터셋 `diamonds` 사용
data(diamonds)

# 데이터의 첫 몇 줄 확인
head(diamonds)

# 4. ggplot2를 사용해 산점도 그리기
# x축: carat, y축: price, 색상: cut(다이아몬드 품질)
ggplot(data = diamonds, aes(x = carat, y = price, color = cut)) +
  geom_point(alpha = 0.7) +  # 점 투명도 설정
  labs(
    title = "다이아몬드 가격과 무게의 관계",
    x = "다이아몬드 무게 (carat)",
    y = "가격 (USD)"
  ) +
  theme_minimal()











# 필요한 패키지 설치
install.packages("readxl")
install.packages("ggplot2")

# 패키지 로드
library(readxl)
library(ggplot2)

# 엑셀 파일 읽기
file_path <- "C:\\Users\\do543\\vs-code-project\\vs-code-project\\my-py\\example-data.xlsx"  # 엑셀 파일 경로
data <- read_excel(file_path, sheet = "Sheet1")  # 첫 번째 시트 읽기

# 데이터 확인
print(data)

# 막대 그래프 생성
ggplot(data, aes(x = Category, y = Value, fill = Category)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  labs(
    title = "Category vs Value",
    x = "Category",
    y = "Value"
  )





# 1. 필요한 패키지 설치 및 로드
install.packages("ggplot2")  # ggplot2 설치
install.packages("factoextra")  # factoextra 설치

library(ggplot2)
library(factoextra)

# 2. 데이터 준비
# mtcars 데이터셋 로드 및 필요한 열 선택
data <- mtcars[, c("mpg", "hp")]  # 연비(mpg)와 마력(hp)만 사용
head(data)  # 데이터 확인

# 3. K-means 클러스터링 수행
set.seed(123)  # 결과의 재현성을 위한 시드 설정
kmeans_result <- kmeans(data, centers = 3, nstart = 25)  # 클러스터 3개 설정

# 클러스터 결과를 데이터에 추가
data$cluster <- as.factor(kmeans_result$cluster)

# 4. 기본 시각화 (ggplot2 사용)
ggplot(data, aes(x = mpg, y = hp, color = cluster)) +
  geom_point(size = 3) +
  theme_minimal() +
  labs(title = "K-means Clustering Visualization",
       x = "Miles Per Gallon (mpg)",
       y = "Horsepower (hp)")

# 5. 클러스터 중심점 추가
centers <- as.data.frame(kmeans_result$centers)  # 클러스터 중심 좌표 추출
ggplot(data, aes(x = mpg, y = hp, color = cluster)) +
  geom_point(size = 3) +
  geom_point(data = centers, aes(x = mpg, y = hp), color = "black", size = 5, shape = 8) +
  theme_minimal() +
  labs(title = "K-means Clustering with Centroids",
       x = "Miles Per Gallon (mpg)",
       y = "Horsepower (hp)")

# 6. factoextra 패키지를 사용한 고급 시각화
fviz_cluster(kmeans_result, data = data[, c("mpg", "hp")],
             geom = "point",          # 데이터 포인트 표시
             ellipse.type = "convex", # 클러스터 경계선 표시
             show.clust.cent = TRUE,  # 클러스터 중심 표시
             main = "Cluster Visualization using factoextra")
