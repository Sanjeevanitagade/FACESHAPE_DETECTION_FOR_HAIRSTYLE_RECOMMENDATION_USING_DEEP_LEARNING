import React, { useState } from 'react';
import axios from 'axios';
import '../styles.css';

const UploadForm = ({ onUploadSuccess }) => {
    const [selectedImage, setSelectedImage] = useState(null);
    const [error, setError] = useState(null);

    const handleImageChange = (event) => {
        const file = event.target.files[0];
        setSelectedImage(file);
    };
    const handleSubmit = async (event) => {
         event.preventDefault();
        if (!selectedImage) {
           setError('Please select an image');
            return;
        }
       setError(null);
        const formData = new FormData();
       formData.append('image', selectedImage);
        try {
            const response = await axios.post('http://localhost:5000/detect_face_shape', formData, {
                headers: { 'Content-Type': 'multipart/form-data' },
            });
           if (response.status === 200) {
                onUploadSuccess(response.data, selectedImage);
           } else {
               setError(`Error uploading the image. Status: ${response.status}`);
          }
       } catch (error) {
           if (error.response) {
               setError(`There was an error in the upload process. Status: ${error.response.status}, message: ${error.response.data}`);
            } else if(error.request) {
                setError(`There was an error in the upload process. No response received from server`);
            } else {
               setError(`There was an error in the upload process. ${error.message}`);
            }
        }
   };
    return (
        <div className="upload-form">
            <form onSubmit={handleSubmit}>
                <label htmlFor="upload-button" className="upload-label">Upload Image</label>
                <input
                   type="file"
                    accept="image/*"
                    onChange={handleImageChange}
                   id="upload-button"
                    style={{ display: 'none' }}
                />
                {selectedImage && <button type="submit" className="detect-button">Detect Now</button>}
                {error && <p className="error-message">{error}</p>}
            </form>
         </div>
    );
};
export default UploadForm;