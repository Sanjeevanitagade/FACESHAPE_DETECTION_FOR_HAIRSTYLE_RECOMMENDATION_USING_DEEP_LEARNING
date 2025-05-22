import React, { useState } from 'react';
import UploadForm from './UploadForm';
import ResultDisplay from './ResultDisplay';
import { useNavigate } from 'react-router-dom';

const HeroSection = () => {
    const [result, setResult] = useState(null);
    const [uploadedImage, setUploadedImage] = useState(null);
    const [currentSlide, setCurrentSlide] = useState(0);
    const slides = [
        { id: 1, title: 'Face Shape Detection for Hairstyle Recommendation', text: 'Welcome to Face Shape Detection for Hairstyle Recommendation. We specialize in analyzing your facial features to suggest the most flattering hairstyles tailored just for you.', image: '/images/slide1.jpg' },
        { id: 2, title: 'Discover Your Perfect Style', text: 'Our advanced tools and expert knowledge help you find the hairstyle that enhances your natural beauty. Let us guide you to a look you will love.', image: '/images/slide2.jpg' }
    ];
    const navigate = useNavigate();

    const prevSlide = () => {
        setCurrentSlide((prevSlide) => (prevSlide - 1 + slides.length) % slides.length);
    };
    const handleImageUploadSuccess = (data, image) => {
        setUploadedImage(image);
        setResult(data);
    };

    const handleRecommendation = () => {
        if (result && result.face_shape && uploadedImage) {
            console.log("Navigating to /recommendation with data:", { faceShape: result.face_shape, image: uploadedImage });
            navigate('/recommendation', {
                state: {
                    faceShape: result.face_shape,
                    image: uploadedImage  // Pass the File object not the created URL.
                }
            });
        }
    }
    return (
        <section className="hero">
            <div className="slider-container">
                <div className="slider" style={{ transform: `translateX(-${currentSlide * 100}%)` }}>
                    {slides.map((slide) => (
                        <div key={slide.id} className="slide" style={{ backgroundImage: `url(${slide.image})` }} >
                            <div className="slide-content">
                                <h1>{slide.title}</h1>
                                <p>{slide.text}</p>
                                {result ? (
                                    <button onClick={handleRecommendation} className="detect-button">Get Hairstyle Recommendation</button>
                                ) : (
                                    <UploadForm onUploadSuccess={handleImageUploadSuccess} />
                                )}
                                {result && <ResultDisplay result={result} image={URL.createObjectURL(uploadedImage)} />}
                            </div>
                        </div>
                    ))}
                </div>
                <button className="prev-button" onClick={prevSlide}></button>
                <button className="next-button" onClick={prevSlide}></button>
            </div>
        </section>
    );
};
export default HeroSection;