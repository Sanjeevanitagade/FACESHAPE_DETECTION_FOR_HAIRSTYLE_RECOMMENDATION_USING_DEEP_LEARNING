import React from 'react';
import '../styles.css';
const ResultDisplay = ({ result, image }) => {
  if (!result) {
    return null;
  }
    return (
     <div className="result-display">
        <h2>Face Shape: {result.face_shape}</h2>
          {result.image_with_landmarks && (
            <div className="image-container">
                 <img src={`data:image/jpeg;base64,${result.image_with_landmarks}`} alt="Processed Face with Landmarks" style={{ maxWidth: '300px' }}/>
             </div>
         )}
     </div>
    );
};
export default ResultDisplay;