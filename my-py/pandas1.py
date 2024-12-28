import pandas as pd

# CSV 파일에서 데이터 읽기
df = pd.read_csv('employee_data.csv')
# print(df.head())  # 데이터의 처음 5행을 출력


# CSV 파일로 쓰기
#index=False 는 인덱스 열을 포함시키지 않겠다는 의미.
df.to_csv('output.csv', index=False)

# 데이터프레임의 정보 확인
# print("==========데이터프레임의 정보 확인==========")
# print(df.info())

# 통계 요약 정보
# print("\n==========통계 요약 정보==========")
# print(df.describe())

# 특정 열 선택
names = df['이름']
# print(names.head())

# 특정 행 선택 (인덱스로) 0이 첫번째 행.
first_row = df.iloc[0]

# 조건을 이용한 필터링
older_than_30 = df[df['나이'] > 30]
# print(older_than_30.head())


# 나이 기준으로 정렬
sorted_df = df.sort_values(by='나이')
# print(sorted_df.head())

# 등록날짜 기준으로 내림차순 정렬
sorted_df_desc = df.sort_values(by='등록날짜', ascending=False)
# print(sorted_df_desc.head())

# 부서별로 그룹화하여 나이의 평균 계산
# grouped_df = df.groupby('부서')['나이'].mean()
# print(grouped_df)

# 결측치 확인
# print(df.isnull().sum())

# 결측치 채우기 fillna 함수 이용(예: 나이의 결측치를 평균 나이로 채우기)
# df['나이'] = df['나이'].fillna(df['나이'].mean())


# 결측치가 있는 행 제거
# df_dropped = df.dropna()

# 결측지 제거확인
# print(df_dropped.isnull().sum())


# 새로운 열 추가
# df['연령대'] = df['나이'].apply(lambda x: '30대' if 30 <= x < 40 else '30대 이하' if x < 30 else '40대 이상')
# print(df.head())

# 열 삭제
# df.drop(columns=['연령대'], inplace=True)
# print(df.head())

# 행 삭제
df.drop(index=[0, 1], inplace=True)  # 첫 두 행 삭제
print(df.head())

# 수정된 데이터를 다시 CSV 파일로 저장
df.to_csv('modified_employee_data.csv', index=False)

# JSON 파일로 저장
df.to_json('modified_employee_data.json', orient='records', force_ascii=False, date_format='iso')
