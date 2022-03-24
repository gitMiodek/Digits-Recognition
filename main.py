from tensorflow import keras
from tensorflow.keras import layers

input_shape = 784
#BUILD A MODEL
model = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=input_shape),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    layers.Dense(128, activation = 'relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.3)
    layers.Dense(10, activation = 'sigmoid')
])
#BUILD A CALLBACK
from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(
    min_delta=0.001,
    patience=20,
    restore_best_weights=True,
)
#BUILD A LEARNING RATE CHANGES
from tensorflow.keras.callbacks import ReduceLROnPlateau
lr_schedule = ReduceLROnPlateau(
    patience=0,
    factor=0.2,
    min_lr=0.001,
)
#MODEL COMPLIE
model.compile(
ptimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']
)
#MODEL FIT
model.fit(
    X_train, y_train,
    validation_data=(X_test,y_test),
    batch_size=256,
    epochs=500
    callbacks = [early_stopping,lr_schedule]
)
