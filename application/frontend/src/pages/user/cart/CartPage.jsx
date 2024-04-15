
import "./CartPage.css";
import Layout from "../../../components/layout/Layout";
import useAuthHeader from "react-auth-kit/hooks/useAuthHeader";
import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Title from "../../../components/layout/Title";
import Product from "../../../components/cart/Product";

/**
 * Cart page that displays all items added to cart from the shop
 * @returns {JSX.Element} The rendered CartPage element
 */
const CartPage = () => {
    const [items, setItems] = useState([]);
    const [total, setTotal] = useState("");
    const [address, setAddress] = useState("");
    const [postalCode, setPostalCode] = useState("");
    const [errors, setError] = useState({});
    const token = useAuthHeader();
    const navigate = useNavigate();

    useEffect(() => {
        axios.get(
            `${import.meta.env.VITE_BACKEND_URL}/api/cart/`, 
            { headers: { Authorization: token } 
        }).then(({ data: { total, items } }) => {
            setItems(items);
            setTotal(total);
        });
    }, []);

    function getTotal() {
        let total = 0;
        items.forEach(item => total += item.subtotal);
        setTotal(total);
    }

    async function checkout() {
        axios.post(
            `${import.meta.env.VITE_BACKEND_URL}/api/cart/checkout/`,
            {address, postal_code: postalCode},
            {headers: {Authorization: token}}
        ).then(() => navigate("/user/orders"))
        .catch(({response: {data}}) => setError(data))
    }

    async function remove(item) {
        axios.put(
            `${import.meta.env.VITE_BACKEND_URL}/api/cart/`,
            {product: item.product_id, quantity: 0},
            {headers: {Authorization: token}}
        ).then(() => {
            items.splice(items.indexOf(item), 1);
            setItems([...items]);
            getTotal();
        })
    }

    return (
        <Layout current="cart">
            <div className="main-cart-container">
                <Title title="Cart" />
                {
                    (items?.length) ?
                    <>
                        <div className="big-cart-box">
                            <div className="cart-item-details-container">
                                <p>Product Details</p>
                                <p>Price</p>
                                <p>Quantity</p>
                                <p>Total Price</p>
                                <p>Remove</p>
                            </div>
                            { items.map(item => <Product key={item.product_id} item={item} getTotal={getTotal} remove={() => remove(item)} />) }
                        </div>
                        <div className="small-cartboxes-container">
                            <div className="small-cartbox-left">
                                <div className="cart-order-summary-header">
                                    <p>Cart Summary</p>
                                </div>
                                <div className="summary-content-container">
                                    <p>Total: ${total}</p>
                                </div>
                                <div className="cart-buttons-container">
                                    <a href="/shop"><button id="grey-button-colour">Keep Shopping</button></a>
                                    <button onClick={checkout}>Checkout</button>
                                </div>
                            </div>
                            <div className="small-cartbox-right" style={{height: "fit-content"}}>
                                <div className="cart-promo-header">
                                    <p>Delivery Details</p>
                                </div>
                                <div style={{width: "100%", textAlign: "start", padding: "20px 30px 20px 30px", display: "grid", gap: 5}}>
                                    <div>
                                        <p>Address</p>
                                        <input value={address} onChange={e => setAddress(e.target.value)} type="text" style={{width: "100%"}} />
                                        { errors.address?.map(error => <div key={errors.address} style={{color: "red"}}>{error}</div>) }
                                    </div>
                                    <div>
                                        <p>Postal Code</p>
                                        <input value={postalCode} onChange={e => setPostalCode(e.target.value)} type="text" style={{width: "100%"}} />
                                        { errors.postal_code?.map(error => <div key={errors.postal_code} style={{color: "red"}}>{error}</div>) }
                                    </div>
                                </div>
                            </div>
                        </div>
                    </> :
                    <div>No products in your cart at the moment... Shop <a href="/shop">here</a> now!</div>
                }
            </div>
        </Layout>
    );
}
export default CartPage;