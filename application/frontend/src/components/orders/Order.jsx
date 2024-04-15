
import Item from "./Item";

/**
 * Order component that standardises the display and returns order details
 * @param {object} order - The details of the order
 * @returns {JSX.Element} The rendered Order element
 */
const Order = ({order}) => {
    return (
        <div style={{border: 1, borderStyle: "solid", borderColor: "black", borderRadius: 10, padding: "15px 20px 15px 20px", textAlign: "start"}}>
            <div><span style={{fontWeight: "bold"}}>Status: </span>{order.order_status}</div>
            <div><span style={{fontWeight: "bold"}}>Address: </span>{order.address}, {order.postal_code}</div>
            <div><span style={{fontWeight: "bold"}}>Date Ordered: </span>{order.date_ordered.split("T")[0]}</div>
            <hr style={{margin: "10px 0px 10px 0px"}} />
            <div style={{display: "flex", flexWrap: "wrap", gap: 10}}>
                { order.items.map(item => <Item key={item.product} item={item} />) }
            </div>
            <hr style={{margin: "10px 0px 10px 0px"}} />
            <div><span style={{fontWeight: "bold"}}>Total: </span>${order.total}</div>
        </div>
    )
}
export default Order;