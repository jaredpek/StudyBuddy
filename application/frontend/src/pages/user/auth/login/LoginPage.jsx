
import { useNavigate } from 'react-router-dom';
import './LoginPage.css';
import useSignIn from 'react-auth-kit/hooks/useSignIn';
import axios from 'axios';
import Layout from "../../../../components/layout/Layout";
import { useState } from 'react';

/**
 * Log in page for existing users to log in
 * @returns {JSX.Element} The rendered LoginPage element
 */
const LoginPage = () => {
    const signIn = useSignIn();
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(false);

    async function login() {
        try {
            const {data: {access}} = await axios.post(
                `${import.meta.env.VITE_BACKEND_URL}/api/user/auth/login/`,
                {username, password}
            )
            signIn({auth: {token: access}});
            navigate("/");
            navigate(0);
        } catch (error) {
            setError(true);
        }
    }

    return (
        <Layout current="login">
        <div className="login-container">

            <div className="login-card">
                <div className="login-header">
                    <p className="login-header-text">Study<span className="blue">Buddy</span></p>
                </div>
                <p>Don't have an account? <a href='/user/auth/register' className="blue directlogin">Register</a></p>

                <div className="login-message">
                    <p className="login-text">Sign In To Your Account</p>
                </div>

                <div style={{color: "red", margin: "15px 0px 20px 0px"}}>{ error && "Incorrect username or password!" }</div>

                <div className="login-inputs" style={{gap: 15}}>
                    <div className="login-input">
                        <p>Username: </p>
                        <input type="username" value={username} onChange={e => setUsername(e.target.value)}></input>
                    </div>
                    <div className="login-input">
                        <p>Password: </p>
                        <input type="password" value={password} onChange={e => setPassword(e.target.value)}></input>
                    </div>
                </div>

                <div className="login-submit-container">
                    <div className="login-submit" onClick={login}>Log In</div>
                </div>
            </div>
            
        </div>

        </Layout>
    );
};
export default LoginPage;