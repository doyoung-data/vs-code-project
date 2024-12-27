import pandas as pd

df = pd.read_csv('employee_data.csv')


print(df.head())
print("===============[1]=============")
print(df.info())
print("===============[2]=============")
print(df.describe())

print("===============[3]=============")

# 이름 데이터 출력
names = df['이름']
print(names)



print("===============[4]=============")
first_row = df.iloc[0]
print(first_row)



print("===============[5]=============")
# 조건을 이용한 필터링
older_than_30 = df[df['나이'] > 30]
print(older_than_30.head())



print("===============[6]=============")
# 나이 기준으로 정렬
sorted_df = df.sort_values(by='나이')
print(sorted_df.head())


print("===============[6]=============")
# 결측치 확인
print(df.isnull().sum())


  