import React, { useState, useEffect } from "react";
import Product from "./Product";

const ShoppingCart = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("https://react-server-k2ig.onrender.com/products");
        const responseData = await response.json();
        setProducts(responseData);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();

    return () => {
      console.log("componentWillUnmount - ShoppingCart");
    };
  }, []);

  const handleIncrement = (product, maxValue) => {
    const updatedProducts = products.map((p) =>
      p.id === product.id && p.quantity < maxValue
        ? { ...p, quantity: p.quantity + 1 }
        : p
    );
    setProducts(updatedProducts);
  };

  const handleDecrement = (product, minValue) => {
    const updatedProducts = products.map((p) =>
      p.id === product.id && p.quantity > minValue
        ? { ...p, quantity: p.quantity - 1 }
        : p
    );
    setProducts(updatedProducts);
  };

  const handleDelete = (product) => {
    if (window.confirm("Please confirm to Delete?")) {
      const updatedProducts = products.filter((p) => p.id !== product.id);
      setProducts(updatedProducts);
    }
  };
  //function to handlepurchase button
  const handlePurchase = (product) => {
    if (window.confirm(`you've successfully purchased your product`)) {
      const updatedProducts = products.map((p) =>
         p.id !== product.id ? { ...p, purchased: true} : p
    );
      setProducts(updatedProducts);
    }
  };

  return (
    <div className="container-fluid" style={{background:'#cccc'}}>
      <h4 style={{textAlign:'center', fontSize:'24px',padding:'7px'}}>Welcome to Shopping #Kart retail therapy at its finest</h4>
      <p style={{textAlign:'center', fontSize:'18px', color:'blueviolet'}}>Bringing home a cart full of happiness</p>
      <div className="row">
        {products.map((item) => (
          <Product
            key={item.id}
            product={item}
            onIncrement={handleIncrement}
            onDecrement={handleDecrement}
            onDelete={handleDelete}
            onPurchase={handlePurchase}
          >
            <button className="btn btn-primary" onClick={handlePurchase}>Purchase</button>
          </Product>
        ))}
      </div>
    </div>
  );
};

export default ShoppingCart;