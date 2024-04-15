/**
 * Title component that standardises the display and renders the respective titles of different pages according to their names correctly
 * @param {string} [title=""] - The title text of the page
 * @returns {JSX.Element} The rendered Title element
 */
const Title = ({title=""}) => {
    return <h1 style={{fontWeight: "bold", fontSize: 40, marginTop: 40, marginBottom: 30}}>{title}</h1>
}
export default Title;