/**
 * StudyArea component that standardises the display and returns details of study areas
 * @param {object} area - The details for the study area
 * @param {string} area.name - The name of the study area
 * @param {string} area.address - The address of the study area
 * @param {string} area.block - The block of the study area
 * @param {string} area.level - The level of the study area
 * @param {string} area.unit_number - The unit number of the study area
 * @param {string} area.open_time - The opening time of the study area
 * @param {string} area.close_time - The closing time of the study area
 * @param {string} area.vacancies - The number of vacancies available in the study area
 * @param {image} area.image - The image of the study area
 * @param {string} area.distance - The distance of the study area from the user
 * @param {boolean} authed - Whether the current user is logged in or not
 * @returns {JSX.Element} The rendered StudyArea element
 */
const StudyArea = ({area, authed}) => {
    return <div className="booking-option-container" style={{padding: 40, display: "flex", gap: 30}}>
        <div className="bookings-first-image" style={{display: "flex", alignItems: "center"}}>
            <img src={`${import.meta.env.VITE_BACKEND_URL}${area.image}`} />
        </div>
        <div className="first-booking-option-details" style={{width: "100%"}}>
            <div style={{display: "flex", gap: 20, alignItems: "center"}}>
                <p className="bookings-location" style={{width: "100%"}}>{area.name}</p>
                { !!area.distance && <h3 className="area-vacancy" style={{height: "fit-content"}}>{area.distance} km</h3> }
            </div>
            <h3 className="area-vacancy">Vacancy: {area.vacancies}</h3>
            <p className="body2-description">{area.block && `Block ${area.block} `}{area.level && `Level ${area.level} `}{area.unit_number && `Room ${area.unit_number}`}</p>
            <p className="body2-description">{area.address}, {area.postal_code}</p>
            <p className="body2-description">{area.open_time} - {area.close_time}</p>
            {authed && <a href={`/study_areas/${area.id}/book`} style={{width: "fit-content"}}><button>Book</button></a>}
        </div>
    </div>
}
export default StudyArea;