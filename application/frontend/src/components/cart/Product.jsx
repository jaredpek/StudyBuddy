import { useEffect, useState } from "react";
import axios from "axios";
import useAuthHeader from "react-auth-kit/hooks/useAuthHeader";
import { RiDeleteBin6Fill } from "react-icons/ri";

/**
 * Product component that renders the product item in the cart page
 * @returns {JSX.Element} The rendered Product element
 */
const Product = ({item, getTotal, remove}) => {
    const [quantity, setQuantity] = useState(item.quantity);
    const [subtotal, setSubtotal] = useState(item.subtotal);
    const token = useAuthHeader();
    let initial = true;

    useEffect(() => {
        if (initial) initial = false;
        item.quantity = Number(quantity);
        item.subtotal = quantity * item.price;
        if (!initial) {
            getTotal();
            update();
        }
        setSubtotal(quantity * item.price);
    }, [quantity])

    async function update() {
        if (quantity > 0) {
            axios.put(
                `${import.meta.env.VITE_BACKEND_URL}/api/cart/`,
                {product: item.product_id, quantity},
                {headers: {Authorization: token}}
            )
        }
    }

    return (
        <div className="cart-item-content-container">
            <div className="cart-item-img-container">
                <img src={`${import.meta.env.VITE_BACKEND_URL}${item.image}`}></img>
            </div>
            <p>${item.price}</p>
            <div className="cart-quantity-container">
                <button onClick={() => {
                    if (Number(quantity) - 1 > 0) setQuantity(Number(quantity) - 1);
                }}>-</button>
                <input min={1} type="number" value={quantity} onChange={e => setQuantity(e.target.value)} style={{width: 60, paddingLeft: 7, paddingRight: 7}} />
                <button onClick={() => setQuantity(Number(quantity) + 1)}>+</button>
            </div>
            <p>${subtotal}</p>
            <button className="cart-remove-button"><RiDeleteBin6Fill color="white" className="cart-remove-icon" size={22} onClick={remove}/></button>
        </div>
    )
}
export default Product;