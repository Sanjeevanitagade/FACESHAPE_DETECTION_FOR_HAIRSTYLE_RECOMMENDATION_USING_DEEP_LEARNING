import React from 'react';
const Testimonials = () => {
    const testimonials = [
        {
            id: 1,
            name: "Mark Jackson",
            text: "Face Shape Detection for Hairstyle Recommendation transformed my look! Their analysis was spot-on, and the hairstyle they suggested perfectly suited my face shape. I felt more confident than ever, and I couldn't be happier with the results.",
            avatar: "/images/avatar1.png"
        },
        {
            id: 2,
            name: "Anna Smith",
            text: "I was amazed by the personalized service I received. The recommendations were tailored to my face shape, and I found a hairstyle that I absolutely love. The team was knowledgeable and made the process enjoyable. Highly recommend!",
            avatar: "/images/avatar2.png"
        },
        {
            id: 3,
            name: "John Champion",
            text: "As someone who struggles with choosing the right hairstyle, I found Face Shape Detection to be a game-changer. Their expert guidance helped me find a cut that enhances my features, and I receive compliments all the time!",
            avatar: "/images/avatar3.png"
        }
    ];

    return (
        <section className="testimonials" id="reviews">
            <h2>Testimonials</h2>
            <div className="testimonial-cards">
                {testimonials.map((testimonial, index) => (
                    <div key={index} className="testimonial-card">
                        <img src={testimonial.avatar} alt="Avatar" className="testimonial-avatar" />
                        <p className="testimonial-name">{testimonial.name}</p>
                        <p className="testimonial-text">“{testimonial.text}”</p>
                    </div>
                ))}
            </div>
        </section>
    );
};

export default Testimonials;