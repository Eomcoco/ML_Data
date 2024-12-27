def my_function(x):
  return 5 * x + 7

val = int(input('숫자를 입력하세요 : '))
ret = my_function(val)
print(ret)


import numpy
from sklearn import linear_model

#1. 데이터, 입력 값과 결과 값
#입력 값 - 2차원임
X_train = numpy.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1,1)

#결과 값 - 정답 1차원임, 입력을 넣었을 나올 정답 (5 * x + 7임을 알아차릴까?)
y_train = numpy.array([12, 17, 22, 27, 32, 37, 42])

#2. 기계학습의 가장 큰 특징 - 어떤 모델을 사용할 것인가 알려줘야 함
model = linear_model.LinearRegression()

#3. 학습
model.fit(X_train, y_train)

#4. 예측
predict = model.predict([[9]])

#예측한 결과 값
print(predict)

import tensorflow as tf

#1. 데이터 지정
X_train = numpy.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1,1)
y_train = numpy.array([12, 17, 22, 27, 32, 37, 42])

#2. 모델 형태 지정
inputs = tf.keras.layers.Input(shape=(1,))  #입력층 입력되는 값이 한 개임(1 dimension)
outputs = tf.keras.layers.Dense(units=1)(inputs)  #출력층

#모델 객체를 생성(특정 모델이 없음)
model = tf.keras.models.Model(inputs, outputs)

#loss 손실함수 -> MeanSquaredError, 최적화 함수(성능이 좋아짐) -> SGD
model.compile(
    loss = tf.keras.losses.MeanSquaredError(),
    optimizer = tf.keras.optimizers.SGD()
)

#3. 모델 학습하기
model.fit(X_train, y_train, epochs=1000, verbose=0)

#4. 예측 epochs = 100 : '55.xx', 1000:52.xx
predict = model.predict(numpy.array([[9]])) #예측값을 numpy 배열 2차원으로 변환

#예측한 결과 값
print(predict)