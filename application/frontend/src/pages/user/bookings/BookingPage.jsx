import '../../study_areas/book/BookSlotPage.css';
import { useEffect, useState } from "react";
import Layout from "../../../components/layout/Layout";
import { useNavigate, useParams } from "react-router-dom";
import useAuthHeader from 'react-auth-kit/hooks/useAuthHeader';
import axios from "axios";
import Title from "../../../components/layout/Title";
import BookingDetails from "../../../components/bookings/BookingDetails";

/**
 * Booking page for users to update an existing booking
 * @returns {JSX.Element} The rendered BookingsPage element
 */
const BookingPage = () => {
    const [booking, setBooking] = useState({});
    const token = useAuthHeader();
    const {booking: id} = useParams();
    const [errors, setErrors] = useState({});
    const navigate = useNavigate();

    useEffect(() => {
        axios.get(
            `${import.meta.env.VITE_BACKEND_URL}/api/bookings/${id}/`,
            {headers: {Authorization: token}}
        ).then(({data}) => {
            setBooking(data);
        })
    }, [])

    async function update() {
        axios.put(
            `${import.meta.env.VITE_BACKEND_URL}/api/bookings/${id}/`, booking,
            {headers: {Authorization: token}}
        ).then(() => navigate("/user/bookings"))
        .catch(({response: {data}}) => {
            if ('non_field_errors' in data) data.non_field_errors = 'Booking already exists';
            setErrors(data);
        })
    }

    return (
        <Layout current="bookings">
            <div className="body">
                <Title title="Update Booking" />
                { !!booking.id && <BookingDetails booking={booking} /> }
                <div style={{margin: "15px 0px 15px"}}>
                    { Object.entries(errors).map(([field, error]) => (field != "status") ? <div key={`${field}_${error}`} style={{color: "red"}}>{field}: {error}</div> : "") }
                </div>
                <div style={{}}>
                    <button onClick={update} style={{cursor: "pointer", backgroundColor: "white", borderRadius: 5, borderColor: "#00bfff", fontSize: 38, width: 300, height: 55, textAlign: "center"}}>Update</button>
                </div>
            </div>
        </Layout>
    )
}
export default BookingPage;