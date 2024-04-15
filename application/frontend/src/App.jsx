import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import useIsAuthenticated from 'react-auth-kit/hooks/useIsAuthenticated';

import './App.css';
import HomePage from './pages/home/HomePage';
import LandingPage from './pages/landing/LandingPage';
import BookSlotPage from './pages/study_areas/book/BookSlotPage';
import LoginPage from './pages/user/auth/login/LoginPage';
import RegisterPage from './pages/user/auth/register/RegisterPage';
import CartPage from './pages/user/cart/CartPage';
import ShopPage from './pages/shop/ShopPage';
import BookingsPage from './pages/user/bookings/BookingsPage';
import StudyAreasPage from './pages/study_areas/StudyAreasPage';
import OrdersPage from './pages/user/orders/OrdersPage';
import BookingPage from './pages/user/bookings/BookingPage';
import BuddyAI from './pages/buddyai/BuddyAI';


function App() {
  const isAuthenticated = useIsAuthenticated();

  return (
    <Router>

      <div className="maincontainer">

        <section id="Home">

           <Routes>
            <Route path="/" element={isAuthenticated ? <HomePage/> : <LandingPage />} />
            <Route path="/shop" element={<ShopPage />} />
            <Route path="/buddyai" element={<BuddyAI />} />
            <Route path="/study_areas" element={<StudyAreasPage />} />
            <Route path="/study_areas/:study_area/book" element={<BookSlotPage />} />
            <Route path="/user/auth/login" element={<LoginPage />} />
            <Route path="/user/auth/register" element={<RegisterPage />} />
            <Route path="/user/cart" element={<CartPage />} />
            <Route path="/user/bookings" element={<BookingsPage />} />
            <Route path="/user/bookings/:booking" element={<BookingPage />} />
            <Route path="/user/orders" element={<OrdersPage />} />
          </Routes>
            
        </section>

      </div>
      
    </Router>
  )
}

export default App
