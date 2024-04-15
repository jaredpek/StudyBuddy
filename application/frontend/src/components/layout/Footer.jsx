import './Footer.css';

/**
 * Footer component that is rendered at the bottom of every page. Displays navigation links and site logo
 * @returns {JSX.Element} The rendered Footer element
 */
const Footer = () => {
    return (
      <div className="footer">
        <div className="footer-section-padding">
            <div className="footer-links">
                <div style={{display: "flex", gap: 30, alignItems: "center", justifyContent: "space-between", width: "100%", flexWrap: "wrap"}}>
                    <div className="footer-links-div">
                        <img src="/SB_black.png" alt="StudyBuddy's logo" style={{maxWidth: 100}} />
                    </div>
                    <div className="footer-links-div">
                        <p className="footer-headers">Links</p>
                        <a href="/"><p>Home</p></a>
                        <a href="/shop"><p>Shop</p></a>
                        <a href="/study_areas"><p>Study Areas</p></a>
                    </div>
                    <div className="footer-links-div">
                        <p className="footer-headers">Contact Us</p>
                        <p>Singapore, Singapore</p>
                        <a><p>studybuddy@gmail.com</p></a>
                    </div>
                </div>
            </div>
        </div>
        <div>Copyright @ StudyBuddy 2024 | All Rights Reserved</div>
      </div>
    );
};
export default Footer;