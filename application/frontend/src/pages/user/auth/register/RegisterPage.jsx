
import './RegisterPage.css';
import Layout from "../../../../components/layout/Layout";
import { useState } from 'react';
import axios from "axios";
import { useNavigate } from 'react-router-dom';
import useSignIn from 'react-auth-kit/hooks/useSignIn';

/**
 * Register page for new users to sign up with StudyBuddy
 * @returns {JSX.Element} The rendered RegisterPage element
 */
const RegisterPage = () => {
    const [username, setUsername] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [mobileNumber, setMobileNumber] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [passwordConfirm, setPasswordConfirm] = useState("");
    const [error, setError] = useState({});

    const navigate = useNavigate();
    const login = useSignIn();

    async function register() {
        axios.post(
            `${import.meta.env.VITE_BACKEND_URL}/api/user/auth/register/`,
            {
                username, email, first_name: firstName, last_name: lastName,
                mobile_number: mobileNumber, password1: password, password2: passwordConfirm
            }
        ).then(({data: {access}}) => {
            login({auth: {token: access}});
            navigate("/");
            navigate(0);
        }).catch(({response: {data}}) => {
            setError(data);
            console.log(data)
        })
    }

    return (
        <Layout current="register">
        <div className="signup-container">
            <div className="signup-card">
                <div className="signup-header">
                    <p className="signup-header-text">Study<span className="blue">Buddy</span></p>
                </div>

                <div className="signup-message">
                    <p className="signup-text">Welcome To Study<span className="blue">Buddy</span></p>
                    <p>Already have an account? <a href='/user/auth/login' className="blue directlogin">Log In</a></p>
                </div>

                <div className="signup-form-container">
                    <div className="signup-container-left">
                        <div className="signup-inputs">
                            <p className="signup-box-label">Username</p>
                            <div className="signup-input">
                                <input value={username} onChange={e => setUsername(e.target.value)}></input>
                                { error.username && error.username.map(err => <div style={{color: "red"}}>{err}</div>) }
                            </div>
                            <div style={{display: "flex", gap: 15}}>
                                <div style={{width: "100%"}}>
                                    <p className="signup-box-label">First Name</p>
                                    <div className="signup-input">
                                        <input value={firstName} onChange={e => setFirstName(e.target.value)} style={{width: "100%"}}></input>
                                        { error.first_name && error.first_name.map(err => <div style={{color: "red", width: 195}}>{err}</div>) }
                                    </div>
                                </div>
                                <div style={{width: "100%"}}>
                                    <p className="signup-box-label">Last Name</p>
                                    <div className="signup-input">
                                        <input value={lastName} onChange={e => setLastName(e.target.value)} style={{width: "100%"}}></input>
                                        { error.last_name && error.last_name.map(err => <div style={{color: "red", width: 195}}>{err}</div>) }
                                    </div>
                                </div>
                            </div>
                            <p className="signup-box-label">Mobile Number</p>
                            <div className="signup-input">
                                <input value={mobileNumber} onChange={e => setMobileNumber(e.target.value)}></input>
                                { error.mobile_number && error.mobile_number.map(err => <div style={{color: "red"}}>{err}</div>) }
                            </div>
                        </div>
                    </div>

                    <div className="signup-container-right">
                        <div className="signup-inputs">
                            <p className="signup-box-label">Email</p>
                            <div className="signup-input">
                                <input type="email" value={email} onChange={e => setEmail(e.target.value)}></input>
                                { error.email && error.email.map(err => <div style={{color: "red"}}>{err}</div>) }
                            </div>
                            <p className="signup-box-label">Password</p>
                            <div className="signup-input">
                                <input type="password" value={password} onChange={e => setPassword(e.target.value)}></input>
                                { error.password1 && error.password1.map(err => <div style={{color: "red"}}>{err}</div>) }
                                { error.non_field_errors && error.non_field_errors.map(err => <div style={{color: "red"}}>{err}</div>) }
                            </div>
                            <p className="signup-box-label">Confirm Password</p>
                            <div className="signup-input">
                                <input type="password" value={passwordConfirm} onChange={e => setPasswordConfirm(e.target.value)}></input>
                                { error.password2 && error.password2.map(err => <div style={{color: "red"}}>{err}</div>) }
                                { error.non_field_errors && error.non_field_errors.map(err => <div style={{color: "red"}}>{err}</div>) }
                            </div>
                        </div>
                    </div>
                </div>
                    
                <div className="signup-submit-container">  
                    <div className="signup-submit" onClick={register}>Register</div>
                </div>
            </div>
        </div>
        </Layout>
    );
};
export default RegisterPage;