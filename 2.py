import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

# Load the ResNet50 model without the top layers (include_top=False)
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 1))

# Freeze the base model layers to prevent them from training initially
base_model.trainable = False

# Add custom layers on top of ResNet50
x = Flatten()(base_model.output)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)  # Dropout rate can be adjusted
output = Dense(3, activation='softmax')(x)  # 3 units for 3 classes (3, 4, 5)

# Create the final model
model = Model(inputs=base_model.input, outputs=output)

# Compile the model with categorical cross-entropy loss and the Adam optimizer
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Set up callbacks for early stopping and learning rate reduction
callbacks = [
    EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True),
    ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=5)
]

# Summary of the model
model.summary()

# The model is now ready to be trained with your data
# Example (replace X_train, y_train, X_val, y_val with your data):
# history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=50, callbacks=callbacks)
