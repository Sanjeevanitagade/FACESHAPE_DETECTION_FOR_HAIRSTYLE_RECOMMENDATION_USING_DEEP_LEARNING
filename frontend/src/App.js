import React from 'react';
import Header from './components/Header';
import HeroSection from './components/HeroSection';
import ServicesSection from './components/ServicesSection';
import Testimonials from './components/Testimonials';
import ContactSection from './components/ContactSection';
import RecommendationPage from './components/RecommendationPage';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './styles.css';

function App() {
    return (
        <Router>
            <div className="app-container">
                <Header />
                <Routes>
                    <Route path="/" element={<HeroSection />} />
                    <Route path="/recommendation" element={<RecommendationPage />} />
                </Routes>
                <ServicesSection />
                <Testimonials />
                <ContactSection />
            </div>
        </Router>
    );
}
export default App;