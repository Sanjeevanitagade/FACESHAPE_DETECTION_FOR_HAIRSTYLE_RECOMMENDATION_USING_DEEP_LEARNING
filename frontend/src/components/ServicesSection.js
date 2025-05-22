import React from 'react';

const ServicesSection = () => {
    return (
        <section className="services" id="services">
            <h2>Learn more about our services</h2>
            <p>At Face Shape Detection for Hairstyle Recommendation, we excel in helping individuals find their ideal hairstyle. Whether you have an oval, round, square, or heart-shaped face, our expert recommendations ensure you achieve a look that suits your features beautifully. Experience the confidence that comes with the perfect hairstyle tailored to you.</p>
            <div className="service-cards">
                <div className="service-card">
                    <h3>Face shape analysis</h3>
                    <p>Using our innovative technology, we perform detailed face shape analyses to provide you with customized hairstyle suggestions that enhance your natural beauty and suit your personal style.</p>
                    <a href="#contact" className="contact-link">Contact </a>
                </div>
                <div className="service-card">
                    <h3>Personalized recommendations</h3>
                    <p>Our team of style experts offers tailored hairstyle recommendations based on your face shape, ensuring that you find a look that not only flatters but also reflects your personality and lifestyle.</p>
                    <a href="#contact" className="contact-link">Contact </a>
                </div>
                <div className="service-card">
                    <h3>Expert advice</h3>
                    <p>At Face Shape Detection for Hairstyle Recommendation, we provide professional advice on hair care and styling techniques, empowering you to maintain your new look with confidence and ease.</p>
                    <a href="#contact" className="contact-link">Contact </a>
                </div>
            </div>
        </section>
    );
};

export default ServicesSection;