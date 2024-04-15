import Layout from "../../../components/layout/Layout";
import useAuthHeader from "react-auth-kit/hooks/useAuthHeader";
import { useEffect, useState } from "react";
import axios from "axios";
import Order from "../../../components/orders/Order";
import Title from "../../../components/layout/Title";

/**
 * Order page that displays all orders successfully made by users
 * @returns {JSX.Element} The rendered OrdersPage element
 */
const OrdersPage = () => {
    const [orders, setOrders] = useState([]);
    const token = useAuthHeader();

    useEffect(() => {
        axios.get(
            `${import.meta.env.VITE_BACKEND_URL}/api/orders/`,
            {headers: {Authorization: token}}
        ).then(({data: {orders}}) => setOrders(orders))
    }, [])

    return (
        <Layout current="orders">
            <Title title={"Orders"} />
            <div style={{display: "grid", gap: 15, marginBottom: 40}}>
                { 
                    orders.length ?
                    orders.map(order => <Order key={order.id} order={order} />) :
                    <div>No orders at the moment... Make an order <a href="/user/cart">here</a> now!</div>
                }
            </div>
        </Layout>
    )
}
export default OrdersPage;