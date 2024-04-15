
import './BookingsPage.css';
import Layout from "../../../components/layout/Layout";
import { useEffect, useState } from 'react';
import useAuthHeader from 'react-auth-kit/hooks/useAuthHeader';
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import Title from '../../../components/layout/Title';
import Booking from '../../../components/bookings/Booking';

/**
 * Bookings page for users to view all their bookings at study areas
 * @returns {JSX.Element} The rendered BookingsPage element
 */
const BookingsPage = () => {
    const [bookings, setBookings] = useState([]);
    const [display, setDisplay] = useState([]);
    const options = ["All", "Ongoing", "Upcoming", "Completed"];
    const [selected, setSelected] = useState(options[0]);
    const token = useAuthHeader();
    const navigate = useNavigate();

    useEffect(() => {
        axios.get(
            `${import.meta.env.VITE_BACKEND_URL}/api/bookings/`,
            {headers: {Authorization: token}}
        ).then(({data: {bookings}}) => {
            setBookings(bookings);
            setDisplay(bookings);
        })
    }, [])

    useEffect(() => {
        if (!bookings.length) return;
        const curr = Date.now();
        let result = bookings.filter(booking => {
            if (selected === options[0]) return true;  // All
            let start = Date.parse(`${booking.date}T${booking.start_time}`), end = Date.parse(`${booking.date}T${booking.end_time}`);
            if (selected === options[1]) return start <= curr && curr <= end;  // Ongoing
            if (selected === options[2]) return curr < start // Upcoming
            return end < curr  // Completed
        });
        setDisplay(result);
    }, [selected])

    async function deleteBooking(id) {
        axios.delete(
            `${import.meta.env.VITE_BACKEND_URL}/api/bookings/${id}/`,
            {headers: {Authorization: token}}
        ).then(() => navigate(0))
    }

    return (
        <Layout current="bookings">
            <Title title={`${selected} Bookings`}/>
            <div style={{margin: "auto", width: "fit-content"}}>
                <ul className="toggle-status-container">
                    { options.map((option) => <li style={{color: (selected === option) ? "#00abe4" : "gray"}} key={option}><a onClick={() => setSelected(option)}>{option.toUpperCase()}</a></li>) }
                </ul>
            </div>
            { 
                display.length ?
                display.map(booking => <Booking key={booking.id} booking={booking} deleteBooking={deleteBooking} />)  :
                <div style={{marginTop: 30}}>No {!!(selected != options[0]) && `${selected.toLowerCase()} `}bookings at the moment... Make a booking <a href='/study_areas'>here</a> now!</div>
            }
        </Layout>
    );
};
export default BookingsPage;