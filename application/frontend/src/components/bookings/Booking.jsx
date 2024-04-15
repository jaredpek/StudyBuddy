/**
 * Booking component that displays the details of a booking
 * @returns {JSX.Element} The rendered Booking element
 */
const Booking = ({booking, deleteBooking}) => {
    return (
        <div className="first-booking-container" style={{padding: 40, display: "flex", gap: 30}}>
            <div className="bookings-first-image">
                <img src={`${import.meta.env.VITE_BACKEND_URL}${booking.image}`} />
            </div>
            <div className="first-booking-details">
                <p className="bookings-date">{booking.date}</p>
                <p className="bookings-area blue">{booking.study_area}</p>
                <p className="bookings-time">{booking.start_time} - {booking.end_time}</p>
                <div style={{display: "flex", gap: 20}}>
                    <a href={`/user/bookings/${booking.id}`}><button>Edit</button></a>
                    <button onClick={() => deleteBooking(booking.id)}>Delete</button>
                </div>
            </div>
        </div>
    )
}

export default Booking;