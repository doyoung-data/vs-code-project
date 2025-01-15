import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical

# 1. 데이터 로드 (예: 영화 감상평 데이터)
# 감상평 데이터가 있다면 아래와 같이 로드합니다. 데이터는 텍스트(감상평)와 레이블(긍정/부정)이 있어야 합니다.
# 예시 데이터프레임 구조: df['review'] (감상평 텍스트), df['sentiment'] (긍정/부정 레이블)

# 데이터 예시
data = {
    'review': [
        "This movie was fantastic!",
        "I hated every minute of it.",
        "Best movie I have seen in a long time.",
        "The plot was dull and uninteresting.",
        "I really enjoyed this film.",
        "It was a total waste of time."
    ],
    'sentiment': ['positive', 'negative', 'positive', 'negative', 'positive', 'negative']
}

df = pd.DataFrame(data)

# 2. 텍스트 전처리
# 레이블을 숫자로 인코딩
label_encoder = LabelEncoder()
df['sentiment'] = label_encoder.fit_transform(df['sentiment'])

# 데이터 나누기 (훈련 및 테스트)
X_train, X_test, y_train, y_test = train_test_split(df['review'], df['sentiment'], test_size=0.2, random_state=42)

# 3. 토크나이저로 텍스트를 숫자로 변환
tokenizer = Tokenizer(num_words=5000)  # 최대 5000개의 단어만 사용
tokenizer.fit_on_texts(X_train)

X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

# 패딩을 사용해 시퀀스 길이를 맞춤
max_sequence_length = 100  # 최대 시퀀스 길이
X_train_pad = pad_sequences(X_train_seq, maxlen=max_sequence_length)
X_test_pad = pad_sequences(X_test_seq, maxlen=max_sequence_length)

# 4. RNN 모델 구축
model = Sequential()

# 임베딩 레이어 (단어를 임베딩 벡터로 변환)
model.add(Embedding(input_dim=5000, output_dim=128, input_length=max_sequence_length))

# LSTM 레이어 추가 (순환 신경망-> RNN)
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))

# 완전 연결층 (출력)
model.add(Dense(1, activation='sigmoid'))

# 5. 모델 컴파일
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 6. 모델 학습
model.fit(X_train_pad, y_train, epochs=5, batch_size=64, validation_data=(X_test_pad, y_test))

# 7. 모델 평가
loss, accuracy = model.evaluate(X_test_pad, y_test)
print(f'Test Accuracy: {accuracy:.4f}')
