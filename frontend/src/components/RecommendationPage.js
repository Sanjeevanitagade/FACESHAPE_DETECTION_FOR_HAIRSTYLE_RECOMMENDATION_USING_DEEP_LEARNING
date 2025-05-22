import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import HairstyleRecommendation from './HairstyleRecommendation';
import '../styles.css';

const RecommendationPage = () => {
    const location = useLocation();
    const navigate = useNavigate();
    const [recommendations, setRecommendations] = useState(null);
    const faceShape = location.state?.faceShape;
    const image = location.state?.image;

    useEffect(() => {
        console.log("RecommendationPage: Received faceShape:", faceShape, "and image:", image);
        if (faceShape) {
            console.log("Fetching hairstyle recommendation for face shape:", faceShape);
            fetch('http://localhost:5000/recommend_hairstyle', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ face_shape: faceShape }),
            })
                .then(response => {
                    console.log("Response received:", response);
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log("Data from backend:", data);
                    if (data && data.hairstyles && Array.isArray(data.hairstyles)) {
                        setRecommendations(data.hairstyles);
                    } else {
                        console.error("Error: Hairstyles data is missing or malformed.");
                        setRecommendations([]);
                    }
                })
                .catch(error => {
                    console.error('Error fetching hairstyles:', error);
                    setRecommendations([]);
                });
        } else {
            console.warn("Face shape is missing, navigating back to home.");
            navigate('/');  // Navigate back to home if faceShape is missing.
        }
    }, [faceShape, navigate]);

    return (
        <div className="recommendation-page">
            <h2>Recommended Hairstyles for {faceShape}</h2>
            {image &&
                <div className="image-container">
                    <img src={URL.createObjectURL(image)} alt="Processed Face with Landmarks" style={{ maxWidth: '300px' }} />
                </div>
            }
            {recommendations && <HairstyleRecommendation recommendations={recommendations} />}
        </div>
    );
};
export default RecommendationPage;