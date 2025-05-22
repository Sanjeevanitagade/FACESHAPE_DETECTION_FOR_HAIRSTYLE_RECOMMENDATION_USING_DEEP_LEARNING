import React from 'react';
import '../styles.css';
const Header = () => {
  return (
    <header className="header">
        <nav className="navbar">
            <div className="logo">Face Shape Detection for Hairstyle Recommendation</div>
            <div className="nav-links">
                <a href="#services">Services</a>
                <a href="#reviews">Reviews</a>
                <a href="#contact">Contacts</a>
            </div>
        </nav>
    </header>
    );
};

export default Header;