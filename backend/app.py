from flask import Flask, request, jsonify
import cv2
import numpy as np
import os
import base64
from utils import detect_face_and_landmarks, get_hairstyle_recommendations, load_dlib_model
from face_shape_classifier import FaceShapeClassifier
from PIL import Image
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

# Initialize Face Shape Classifier and models
try:
    face_shape_classifier = FaceShapeClassifier('../models/face_shape_classifier.h5')
    face_detector, landmark_predictor = load_dlib_model()
    print("Models loaded successfully.")
except Exception as e:
    print(f"Error loading models: {e}")
    face_shape_classifier = None
    face_detector = None
    landmark_predictor = None

@app.route('/detect_face_shape', methods=['POST'])
def detect_face_shape():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        # Read the image file from the request
        image_file = request.files['image']
        image_data = image_file.read()
        image_bytes = io.BytesIO(image_data)
        
        # Convert image to OpenCV format
        image = Image.open(image_bytes)
        image = np.array(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Detect face and landmarks
        if face_detector is None or landmark_predictor is None:
            return jsonify({'error': 'Face detection model not loaded properly'}), 500

        image_with_landmarks, landmarks, face_coords = detect_face_and_landmarks(image.copy(), face_detector, landmark_predictor)
        if image_with_landmarks is None:
            return jsonify({'error': 'No face detected'}), 400
        
        # Predict face shape
        if face_shape_classifier is None:
            return jsonify({'error': 'Face shape classifier not loaded properly'}), 500
        
        face_shape = face_shape_classifier.predict(image.copy())
        
        # Encode image with landmarks to base64
        _, buffer = cv2.imencode('.jpg', image_with_landmarks)
        image_base64 = base64.b64encode(buffer).decode('utf-8')
        
        return jsonify({
            'face_shape': face_shape,
            'landmarks': landmarks,
            'face_coords': face_coords,
            'image_with_landmarks': image_base64
        })
    except Exception as e:
        print(f"Error in detect_face_shape endpoint: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/recommend_hairstyle', methods=['POST'])
def recommend_hairstyle():
    try:
        data = request.get_json()
        if not data or 'face_shape' not in data:
            return jsonify({'error': 'Face shape is required'}), 400
        
        face_shape = data.get('face_shape')
        
        # Get hairstyle recommendations based on face shape
        recommendations = get_hairstyle_recommendations(face_shape)
        
        if not recommendations['hairstyles']:
            return jsonify({'error': 'No recommendations found for this face shape'}), 404
        
        return jsonify({'hairstyles': recommendations['hairstyles']})
    except Exception as e:
        print(f"Error in recommend_hairstyle endpoint: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)