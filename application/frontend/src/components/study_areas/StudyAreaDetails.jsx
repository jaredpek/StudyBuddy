/**
 * StudyAreaDetails component that standardises the display and returns details of study areas
 * @param {object} area - The details of the study area
 * @param {string} area.name - The name of the study area
 * @param {string} area.address - The address of the study area
 * @param {string} area.block - The block of the study area
 * @param {string} area.level - The level of the study area
 * @param {string} area.unit_number - The unit number of the study area
 * @param {string} area.open_time - The opening time of the study area
 * @param {string} area.close_time - The closing time of the study area
 * @param {string} area.vacancies - The number of vacancies available in the study area
 * @returns {JSX.Element} The rendered StudyAreaDetails element
 */
const StudyAreaDetails = ({area}) => {
    return (
        <>
            <div className="body2-content-header">
                <h2 className="body2-title">{area.name}</h2>
                <h3 className="body2-vacancy">Vacancy: {area.vacancies}</h3>
            </div>
            <p className="body2-description">{area.block && `Block ${area.block} `}{area.level && `Level ${area.level} `}{area.unit_number && `Room ${area.unit_number}`}</p>
            <p className="body2-description">{area.address}, {area.postal_code}</p>
            <p className="body2-description">{area.open_time} - {area.close_time}</p>
            <div style={{marginTop: 20, fontWeight: "bold"}}>Each slot will last 1 hour, but you may book multiple slots</div>
        </>
    )
}
export default StudyAreaDetails;