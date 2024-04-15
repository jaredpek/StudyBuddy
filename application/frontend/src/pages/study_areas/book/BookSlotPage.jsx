
import "./BookSlotPage.css";
import Layout from "../../../components/layout/Layout";
import { useNavigate, useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import useAuthHeader from 'react-auth-kit/hooks/useAuthHeader';
import axios from "axios";
import Title from "../../../components/layout/Title";
import BookingForm from "../../../components/bookings/BookingForm";
import StudyAreaDetails from "../../../components/study_areas/StudyAreaDetails";

/**
 * Booking of slot page that lets users confirm their availabilities and bookings
 * @returns {JSX.Element} The rendered BookSlotPage element
 */
const BookSlotPage = () => {
    const {study_area} = useParams();
    const [area, setArea] = useState({});
    const [booking] = useState({});
    const [errors, setErrors] = useState({});
    const navigate = useNavigate();
    const token = useAuthHeader();

    useEffect(() => {
        axios.get(`${import.meta.env.VITE_BACKEND_URL}/api/study_areas/${study_area}/`)
        .then(({data}) => setArea(data))
    }, [])

    async function book() {
        const {date, start_time, end_time} = booking;
        const err = {};
        if (!date) err.date = "This field must not be blank.";
        if (!start_time) err.start_time = "This field must not be blank.";
        if (!end_time) err.end_time = "This field must not be blank.";
        if (Object.entries(err).length) {
            setErrors(err)
            return;
        }
        axios.post(
            `${import.meta.env.VITE_BACKEND_URL}/api/bookings/`,
            {date, study_area, start_time, end_time},
            {headers: {Authorization: token}}
        ).then(() => navigate("/user/bookings"))
        .catch(({response: {data}}) => {
            if ('non_field_errors' in data) data.non_field_errors = 'Booking already exists';
            setErrors(data);
        })
    }

    return (
        <Layout current="study_areas">
            <div className="bookslot-body">
                <Title title="Book a Slot" />
                <div className="bookslot-body2">
                    <img className="bookslot-first-image" src={`${import.meta.env.VITE_BACKEND_URL}${area.image}`} />
                    <div className="bookslot-body2-content">
                        <StudyAreaDetails area={area} />
                        <BookingForm booking={booking} />
                    </div>
                </div>
                <div style={{margin: "15px 0px 15px 0px"}}>
                    { Object.entries(errors).map(([field, error]) => (field != "status") ? <div key={`${field}_${error}`} style={{color: "red"}}>{field}: {error}</div> : "") }
                </div>
                <div className="bookslot-body3">
                    <button onClick={book}>Confirm</button>
                </div>
            </div>
        </Layout>
    );
};
export default BookSlotPage;