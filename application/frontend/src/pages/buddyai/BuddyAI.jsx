
import { useState } from "react";
import Layout from "../../components/layout/Layout";
import Title from "../../components/layout/Title";
import axios from "axios";
import { ClipLoader } from "react-spinners";
import useAuthHeader from "react-auth-kit/hooks/useAuthHeader";

/**
 * BuddyAI page that leverages on AI to help users with their homework
 * @returns {JSX.Element} The rendered BuddyAI element
 */
const BuddyAI = () => {
    const [question, setQuestion] = useState("");
    const [response, setResponse] = useState("");
    const [loading, setLoading] = useState(false);
    const token = useAuthHeader();

    async function ask() {
        if (loading || !question) return;
        setLoading(true);
        axios.post(
            `${import.meta.env.VITE_BACKEND_URL}/api/buddy/`, {question},
            {headers: {Authorization: token}}
        ).then(({data: {answer}}) => setResponse(answer))
        .catch((err) => console.log(err))
        .finally(() => setLoading(false));
    }

    return (
        <Layout current="buddyai">
            <Title title="BuddyAI" />
            <div>Need help with your homework? Let BuddyAI help you!</div>
            <div style={{margin: "20px 0px 20px"}}>
                <div style={{fontWeight: "bold"}}>Question:</div>
                <textarea
                    style={{width: "100%", borderRadius: 10, minHeight: 100, padding: 10, resize: "vertical"}}
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                />
                <button
                    style={{background: "#00abe4", color: "white", borderRadius: 10, padding: "15px 20px 15px 20px", border: 1, borderStyle: "solid", cursor: (loading) ? "not-allowed" : "pointer"}}
                    onClick={ask}
                >
                    Ask Buddy
                </button>
            </div>
            { loading && <ClipLoader color="grey" size={30} /> }
            {
                !!response && !loading &&
                <div>
                    <div style={{fontWeight: "bold"}}>Buddy's Response:</div>
                <textarea
                    style={{width: "100%", borderRadius: 10, minHeight: 500, padding: 10, resize: "vertical"}}
                    value={response}
                    readOnly={true}
                />
                </div>
            }
        </Layout>
    )
}
export default BuddyAI;