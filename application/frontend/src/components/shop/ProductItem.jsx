
import React, { useState } from 'react';
import useIsAuthenticated from 'react-auth-kit/hooks/useIsAuthenticated';
import useAuthHeader from 'react-auth-kit/hooks/useAuthHeader';
import axios from "axios";

/**
 * ProductItem component that displays products available in the shop to users
 * @param {object} product - The details of the product
 * @param {string} product.id - The id of the product
 * @param {string} product.price - The price of the product
 * @param {image} product.image - The image of the product
 * @returns {JSX.Element} The rendered ProductItem element
 */
const ProductItem = ({ product }) => {
    const isAuthenticated = useIsAuthenticated();
    const token = useAuthHeader();
    const [added, setAdded] = useState(false);

    function add() {
        axios.post(
            `${import.meta.env.VITE_BACKEND_URL}/api/cart/`,
            {product: product.id, quantity: 1},
            {headers: {Authorization: token}}
        ).catch(err => console.log(err))
        .finally(() => {
            setAdded(true);
            setTimeout(() => setAdded(false), 500);
        });
    }

    return (
        <div className="shop-item-card">
            <img src={`${import.meta.env.VITE_BACKEND_URL}${product.image}`} alt="Product" className="shop-item-image" />
            <h3 className="shop-item-name">{product.name}</h3>
            <p className="shop-item-price">${product.price}</p>
            {isAuthenticated && <button className="shop-item-button" onClick={add}>Add{added && "ed"} To Cart{added && "!"}</button>}
        </div>
    );
};

export default ProductItem;