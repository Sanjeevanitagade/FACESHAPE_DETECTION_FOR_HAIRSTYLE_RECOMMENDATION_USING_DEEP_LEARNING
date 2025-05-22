import React from 'react';
const ContactSection = () => {
    return (
      <section className="contact" id="contact">
        <div className="contact-content">
          <h2>Contact us</h2>
          <div className="contact-info">
             <div className="contact-item">
                <img src="/images/phone.png" alt="Contacts" />
                 <div className="contact-details">
                     <h4>Contacts</h4>
                    <p>faceshapeinfo@gmail.com</p>
                    <p>+91 1234567890</p>
                 </div>
             </div>
             <div className="contact-item">
                <img src="/images/location.png" alt="Location" />
                 <div className="contact-details">
                    <h4>Location</h4>
                   <p>Mumbai</p>
                    <p>India</p>
                </div>
            </div>
            <div className="contact-item">
               <img src="/images/time.png" alt="Working hours" />
                <div className="contact-details">
                    <h4>Working hours</h4>
                   <p>Open: 12:00 pm</p>
                    <p>Closed: 22:00 pm</p>
                 </div>
             </div>
           </div>
          <div className="subscribe-area">
                <h4>Get our latest updates</h4>
               <div className="subscribe-form">
                 <input type="email" placeholder="Enter your email" />
                   <button>Subscribe</button>
                </div>
            </div>
            <p className="copyright">© All Rights Reserved. Face Shape Detection for Hairstyle Recommendation</p>
         </div>
    </section>
   );
};

export default ContactSection;