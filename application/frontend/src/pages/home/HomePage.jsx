
import "./HomePage.css";
import { HiOutlineMagnifyingGlass } from "react-icons/hi2";
import Layout from "../../components/layout/Layout";
import { useEffect, useState } from "react";
import useAuthHeader from "react-auth-kit/hooks/useAuthHeader";
import axios from "axios";
import { MdOutlineShoppingCart } from "react-icons/md";
import { FaChalkboardTeacher } from "react-icons/fa";

/**
 * Home page that welcomes users back post login
 * @returns {JSX.Element} The rendered HomePage element
 */
const HomePage = () => {
    const [name, setName] = useState("");
    const token = useAuthHeader();

    useEffect(() => {
        axios.get(
        `${import.meta.env.VITE_BACKEND_URL}/api/user/profile/`,
        {headers: {Authorization: token}}
        ).then(({data: {first_name}}) => setName(first_name.toLowerCase()))
    }, [])

    return (
        <Layout current="home">
            <div className="pl-body1">
                <div className="pl-post-container1">
                    <div className="pl-post-content1">
                        <p className="blue">Welcome back, <span style={{textTransform: "capitalize"}}>{name}</span>!</p>
                    </div>
                    <div className="pl-post-content2">
                        <p className="linebreak">Whats on your mind today?</p>
                    </div>
                </div>
            </div>

            <div className="pl-body2">
                <div className="pl-post-container2">
                    <a className="card" href="/study_areas">
                        <p className="card-content">Browse Study Areas</p>
                        <HiOutlineMagnifyingGlass size={70} color="black" />
                    </a>
                    <a className="card" href="/shop">
                        <p className="card-content">Browse Products</p>
                        <MdOutlineShoppingCart size={70} color="black" />
                    </a>
                    <a className="card" href="/buddyai">
                        <p className="card-content">Ask AI Buddy</p>
                        <FaChalkboardTeacher size={70} color="black" />
                    </a>
                </div>
            </div>
            </Layout>
    );
};
export default HomePage;