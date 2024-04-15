
import "./LandingPage.css";
import Layout from "../../components/layout/Layout";

/**
 * Landing page that displays information about StudyBuddy to welcome users
 * @returns {JSX.Element} The rendered LandingPage element
 */
const LandingPage = () => {
  return (
    <Layout current="home">
        <div className="body1">
            <div className="landing-body-container1">
                <div className="landing-body1-content">
                    <p className="linebreak">Find, Book, & Purchase,</p>
                    <p className="blue">All In One Place</p>
                    <div style={{marginBottom: 10}}><a href="/study_areas"><button>Book Here</button></a></div>
                    <a href="/shop"><button>Shop Here</button></a>
                </div>
                <div className="landing-image-container">
                    <div><img className="landing-first-image" src="/study-image-1.jpg"/></div>
                </div>
            </div>
        </div>

        <div className="body2">
            <div className="landing-body-container2">
                <div className="landing-image-container">
                    <div><img className="landing-second-image" src="/study-image-2.jpg"/></div>
                </div>
                <div className="landing-body2-content">
                        <p className="blue linebreak about-heading">About Us</p>
                        <p className="linebreak text">With StudyBuddy, locate a study area at your</p>
                        <p className="linebreak text">convenience with ease. Find a conducive area near</p>
                        <p className="linebreak text">where you are and at your preferred time. Join us</p>
                        <p className="text">today!</p>
                        <a href="/user/auth/register"><button>Register</button></a>
                </div>
            </div>
        </div>

        <div className="body3">
            <div className="landing-body-container3">
                <div className="landing-body3-content">
                        <p className="blue linebreak browse-heading">Browse Our Online Store</p>
                        <p className="linebreak text">Be it stationery, books, or any other learning</p>
                        <p className="linebreak text">equipment. You name it, we have it. Browse our</p>
                        <p className="linebreak text">online store and be sure not to miss out on our</p>
                        <p className="text">deals!</p>
                </div>
                <div className="landing-image-container">
                    <div><img className="landing-third-image" src="/stationery-image.jpg"/></div>
                </div>
            </div>
        </div>
    </Layout>
  );
};
export default LandingPage;