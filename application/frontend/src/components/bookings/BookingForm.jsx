
import { useEffect, useState } from "react";

/**
 * BookingForm component that displays the booking form for users to input their preferred booking date, start time, and end time
 * @returns {JSX.Element} The rendered BookingForm element
 */
const BookingForm = ({booking={}}) => {
    const [date, setDate] = useState(booking.date || "");
    const [startTime, setStartTime] = useState(booking.start_time || "");
    const [endTime, setEndTime] = useState(booking.end_time || "");

    useEffect(() => {
        if (!startTime) return;
        let hour = Number(startTime.split(":")[0]);
        setEndTime((hour == 23) ? `00:00` : (hour < 9) ? `0${hour + 1}:00` : `${hour + 1}:00`);
    }, [startTime])

    useEffect(() => {
        booking.date = date;
        booking.start_time = startTime;
        booking.end_time = endTime;
    }, [date, startTime, endTime])

    return (
        <ul className="booking-settings-container">
            <li style={{fontWeight: "initial"}}>Date: <input type="date" style={{width: "fit-content"}} value={date} onChange={e => setDate(e.target.value)} /></li>
            <li style={{fontWeight: "initial"}}>Start: <input step={3600} type="time" style={{width: "fit-content"}} value={startTime} onChange={e => setStartTime(e.target.value)} /></li>
            <li style={{fontWeight: "initial"}}>End: <input step={3600} disabled={true} type="time" style={{width: "fit-content"}} value={endTime} onChange={e => setEndTime(e.target.value)} /></li>
        </ul>
    )
}
export default BookingForm;