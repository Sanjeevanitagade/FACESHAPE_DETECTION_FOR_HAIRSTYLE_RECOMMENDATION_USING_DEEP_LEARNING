import React from 'react';
import '../styles.css';

const HairstyleRecommendation = ({ recommendations }) => {
    if (!recommendations) {
        return <p>Loading hairstyle recommendations...</p>;
    }

    if (!Array.isArray(recommendations) || recommendations.length === 0) {
        return <p>No hairstyle recommendations found for this face shape.</p>;
    }

    return (
        <div className="recommendation-list">
            <h2>Hairstyle Recommendations</h2>
            <div className="recommendations">
                {recommendations.map((hairstyle, index) => (
                    <div key={index} className="recommendation-card">
                        <h3>{hairstyle.name}</h3>
                        <p>{hairstyle.description}</p>
                        <img src={hairstyle.image} alt={hairstyle.name} style={{ maxWidth: '150px' }} />
                    </div>
                ))}
            </div>
        </div>
    );
};
export default HairstyleRecommendation;