import pandas as pd

# 예시 데이터 생성
# 딕셔너리의 key의 타입은 문자열, value의 타입은  리스트[] 로 표현한다.
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 생성된 데이터프레임 출력
# print(df)

#City 로 그룹화 하고 Age의 평균 값 계산
city_group = df.groupby('City')['Age'].mean()

# print(city_group)

# 예제 데이터프레임 생성
df1 = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 24, 35]
})

df2 = pd.DataFrame({
    'Name': ['John', 'Anna', 'Linda'],
    'City': ['New York', 'Paris', 'London']
})

# 'Name' 열을 기준으로 병합
merged_df = pd.merge(df1, df2, on='Name')

print(merged_df)