
import "./ShopPage.css";
import ProductItem from "../../components/shop/ProductItem";
import Layout from "../../components/layout/Layout";
import { useEffect, useState } from "react";
import axios from "axios";
import useIsAuthenticated from 'react-auth-kit/hooks/useIsAuthenticated';
import Title from "../../components/layout/Title";

/**
 * ShopPage component that renders the stationery shop for users to purchase items
 * @returns {JSX.Element} The rendered ShopPage element
 */
const ShopPage = () => {
    const [products, setProducts] = useState([]);
    const isAuthenticated = useIsAuthenticated();

    useEffect(() => {
        axios.get(`${import.meta.env.VITE_BACKEND_URL}/api/products/`)
        .then(({data: {products}}) => setProducts(products))
    }, [])

  return (
    <Layout current="shop">
      <Title title="Products" />
      {!isAuthenticated && <div style={{marginBottom: 15}}>Please login to add items to your cart!</div>}
      <div className="shop-item-container">  
        { products.map(product => <ProductItem key={product.id} product={product} />) }
      </div>
    </Layout>
  );
};
export default ShopPage;