import './AuthNavBar.css';
import { useNavigate } from 'react-router-dom';
import useSignOut from 'react-auth-kit/hooks/useSignOut';
import useAuthHeader from "react-auth-kit/hooks/useAuthHeader";
import { useEffect, useState } from 'react';
import axios from "axios";

/**
 * Navigation bar component that is rendered after users log into their accounts. Displays navigation links and user information
 * @param {string} current - The current page
 * @returns {JSX.Element} The rendered AuthNavBar element
 */
const AuthNavBar = ({current}) => {
  const navigate = useNavigate();
  const signOut = useSignOut();
  const token = useAuthHeader();
  const [name, setName] = useState("");

  useEffect(() => {
    axios.get(
      `${import.meta.env.VITE_BACKEND_URL}/api/user/profile/`,
      {headers: {Authorization: token}}
    ).then(({data: {first_name}}) => setName(first_name.toLowerCase()))
  }, [])

  function logout() {
    signOut();
    navigate("/");
    navigate(0);
  }

  return (
    <>
      <nav>
          <p><a href="/">Study<span className="blue">Buddy</span></a></p>

          <ul className="navbar-links" id="middle">
              <li><a href="/" className={(current === "home") ? "active" : ""}>Home</a></li>
              <li><a href="/study_areas" className={(current === "study_areas") ? "active" : ""}>Study Areas</a></li>
              <li><a href="/user/bookings" className={(current === "bookings") ? "active" : ""}>Bookings</a></li>
              <li><a href="/shop" className={(current === "shop") ? "active" : ""}>Shop</a></li>
              <li><a href="/user/cart" className={(current === "cart") ? "active" : ""}>Cart</a></li>
              <li><a href="/user/orders" className={(current === "orders") ? "active" : ""}>Orders</a></li>
              <li><a href="/buddyai" className={(current === "buddyai") ? "active" : ""}>BuddyAI</a></li>
          </ul>
          
          <div className="user-container navbar-links" style={{flexShrink: 0}}>
            <div className="blue-circle"></div>
            <div className="name" style={{textTransform: "capitalize"}}>{name}</div>
            <button onClick={logout}>Logout</button>
          </div>
          
      </nav>
    </>
  );
};
export default AuthNavBar;