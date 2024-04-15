import './PublicNavBar.css';

/**
 * Navigation bar component that is rendered before users log into their accounts. Displays navigation links and options to sign up or log in
 * @param {string} current - The current page open
 * @returns {JSX.Element} The rendered PublicNavBar element
 */
const PublicNavBar = ({current}) => {
    return (
    <>
        <nav>
            <p><a href='/'>Study<span className="blue">Buddy</span></a></p>

            <ul className="navbar-links" id="middle">
                <li><a href="/" className={(current === "home") ? "active" : ""}>Home</a></li>
                <li><a href="/study_areas" className={(current === "study_areas") ? "active" : ""}>Study Areas</a></li>
                <li><a href="/shop" className={(current === "shop") ? "active" : ""}>Shop</a></li>
            </ul>

            <ul className="navbar-links" id="right" style={{flexShrink: 0}}>
                <li><a href="/user/auth/login" className={(current === "login") ? "active" : ""}>Log In</a></li>
                <a href="/user/auth/register"><button>Register</button></a>
            </ul>
        </nav>
    </>
    );
};
export default PublicNavBar;