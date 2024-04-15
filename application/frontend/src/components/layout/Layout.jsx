import Footer from "./Footer";
import PublicNavbar from "./PublicNavBar";
import AuthNavBar from "./AuthNavBar";
import useIsAuthenticated from 'react-auth-kit/hooks/useIsAuthenticated';

/**
 * Layout component that renders the common layout structure of the webpage. Renders the correct navigation bar based on whether users have authenticated correctly
 * @param {object} children - All the child elements of the page
 * @param {string} [current=""] - The current page open
 * @returns {JSX.Element} The rendered Layout element
 */
const Layout = ({children, current=""}) => {
    const isAuthenticated = useIsAuthenticated();
    return (
        <>
            { isAuthenticated ? <AuthNavBar current={current} /> : <PublicNavbar current={current} /> }
            {children}
            <Footer />
        </>
    )
}
export default Layout;