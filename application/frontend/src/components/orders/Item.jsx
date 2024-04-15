/**
 * Item component that standardises the display and returns item details
 * @param {object} item - The details of the item
 * @returns {JSX.Element} The rendered Item element
 */
const Item = ({item}) => {
    return (
        <div style={{border: 1, borderStyle: "solid", borderColor: "black", borderRadius: 10, padding: 15}}>
            <div style={{display: "flex", gap: 10, alignItems: "center"}}>
                <span style={{fontSize: 20}}>{item.quantity}x</span><img style={{height: 150}} src={`${import.meta.env.VITE_BACKEND_URL}${item.image}`} />
            </div>
            <hr style={{marginTop: 10, marginBottom: 10}} />
            <div><span style={{fontWeight: "bold"}}>Unit Price: </span>${item.price}</div>
            <div><span style={{fontWeight: "bold"}}>Subtotal: </span>${item.subtotal}</div>
        </div>
    )
}
export default Item;