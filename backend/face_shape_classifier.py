import tensorflow as tf
import cv2
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.applications.vgg16 import preprocess_input

class FaceShapeClassifier:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.face_shapes = ["oval", "heart", "square", "long", "round"]
        self.label_encoder = LabelEncoder()
        self.label_encoder.fit(self.face_shapes)

    def preprocess_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (128, 128))
        image = image.astype('float32')
        image = np.expand_dims(image, axis=0)
        image = preprocess_input(image)  # Preprocess for VGG16
        return image

    def predict(self, image):
        preprocessed_image = self.preprocess_image(image)
        predictions = self.model.predict(preprocessed_image)
        predicted_label_encoded = np.argmax(predictions, axis=1)[0]
        predicted_label = self.label_encoder.inverse_transform([predicted_label_encoded])[0]
        return predicted_label