
import { useEffect, useState } from "react";
import StudyAreaDetails from "../study_areas/StudyAreaDetails";
import BookingForm from "./BookingForm";
import axios from "axios";

/**
 * BookingDetails component that displays the details of a booking. It fetches the details of the study area connected to the booking and renders StudyAreaDetails and BookingForm
 * @returns {JSX.Element} The rendered BookingDetails element
 */
const BookingDetails = ({booking}) => {
    const [area, setArea] = useState({});

    useEffect(() => {
        axios.get(`${import.meta.env.VITE_BACKEND_URL}/api/study_areas/${booking.study_area_id}`)
        .then(({data}) => setArea(data))
    }, [])

    return (
        <div className="bookslot-body2" style={{alignItems: "center"}}>
            <img className="first-image" src={`${import.meta.env.VITE_BACKEND_URL}${area.image}`} style={{width: 413, height: 245, borderRadius: 15}} />
            <div className="body2-content">
                <StudyAreaDetails area={area} />
                <BookingForm booking={booking} />
            </div>
        </div>
    )
}
export default BookingDetails;