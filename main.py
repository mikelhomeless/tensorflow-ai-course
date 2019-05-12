import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

def df_to_dataset(data, shuffle=True, batch_size=32):
  data = data.copy()
  labels = data.pop('target')
  data_set = tf.data.Dataset.from_tensor_slices((dict(data), labels))
  if shuffle:
    data_set = data_set.shuffle(buffer_size=len(data))
  data_set = data_set.batch(batch_size)
  return data_set

data = pd.read_csv('heart.csv')
data.head()

training, test = train_test_split(data, test_size=0.2)
training, val = train_test_split(training, test_size=0.2)

batch_size = 32
training_data_Set = df_to_dataset(training, batch_size=batch_size)
validation_data_set = df_to_dataset(val, shuffle=False, batch_size=batch_size)
test_data_set = df_to_dataset(test, shuffle=False, batch_size=batch_size)

feature_columns = []

# numeric columns
for column_name in ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'slope', 'ca']:
  feature_columns.append(feature_column.numeric_column(column_name))

# Setup one hot columns
sex = feature_column.categorical_column_with_vocabulary_list(
    'sex', [0, 1]
)
sex_one_hot = feature_column.indicator_column(sex)
feature_columns.append(sex_one_hot)

cp = feature_column.categorical_column_with_vocabulary_list(
    'cp', [0, 1, 2, 3]
)
cp_one_hot = feature_column.indicator_column(cp)
feature_columns.append(cp_one_hot)

restecg = feature_column.categorical_column_with_vocabulary_list(
    'restecg', [0, 1, 2]
)
restecg_one_hot = feature_column.indicator_column(restecg)
feature_columns.append(restecg_one_hot)

thal = feature_column.categorical_column_with_vocabulary_list(
    'thal', [1, 2, 3]
)
thal_one_hot = feature_column.indicator_column(thal)
feature_columns.append(thal_one_hot)

fbs = feature_column.categorical_column_with_vocabulary_list(
    'fbs', [0, 1]
)
fbs_one_hot = feature_column.indicator_column(fbs)
feature_columns.append(fbs_one_hot)

feature_layer = tf.keras.layers.DenseFeatures(feature_columns)

model = tf.keras.Sequential([
  feature_layer,
  layers.Dense(128 , activation='sigmoid'),
  layers.Dense(128, activation='sigmoid'),
  layers.Dense(32, activation='relu'),
  layers.Dense(25, activation='relu'),
  layers.Dense(1, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_data_Set,
          validation_data=validation_data_set,
          epochs=5)

loss, accuracy = model.evaluate(test_data_set)
print("Accuracy", accuracy)
