import React, { useState } from "react";

function Dashboard() {
  const [query, setQuery] = useState("");
  const [products, setProducts] = useState([]);

  const handleSearch = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch(`http://localhost:5000/search?q=${query}`);
      const data = await response.json();
      setProducts(data);
    } catch (error) {
      console.error("Error fetching search results:", error);
    }
  };

  return (
    <>
      <form onSubmit={handleSearch}>
        <input
          type="text"
          id="search-input"
          placeholder="search for products"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button id="search-button" type="submit">Search...</button>
      </form>

      <h5>We deal with products of various varieties 😊</h5>

      <div className="images">
        {products.length > 0 ? (
          products.map((product) => (
            <div className="image" key={product.id}>
              <img
                className="img-fluid"
                src={product.imageUrl}
                alt={product.nameOfProduct}
              />
              <p className="text-center text-primary">{product.nameOfProduct}</p>
              <p className="text-center text-secondary">Price: {product.price}</p>
            </div>
          ))
        ) : (
          <>
            <div className="image">
              <img
                className="img-fluid"
                src="https://images.unsplash.com/photo-1557825835-b4527f242af7?w=1400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fHRhYmxldHxlbnwwfHwwfHx8MA%3D%3D"
                alt="tab"
              />
              <p className="text-center text-primary">Tablets</p>
            </div>

            <div className="image">
              <img
                className="img-fluid"
                src="https://images.unsplash.com/photo-1605170439002-90845e8c0137?w=1400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHBob25lc3xlbnwwfHwwfHx8MA%3D%3D"
                alt="src2"
              />
              <p className="text-center text-primary">Phones</p>
            </div>

            <div className="image">
              <img
                className="img-fluid"
                src="https://images.unsplash.com/photo-1623126908029-58cb08a2b272?w=1400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fHRhYmxldHxlbnwwfHwwfHx8MA%3D%3D"
                alt="src"
              />
              <p className="text-center text-primary">Phones</p>
            </div>

            <div className="image">
              <img
                className="img-fluid"
                src="https://images.unsplash.com/photo-1609252925148-b0f1b515e111?w=1400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fHBob25lc3xlbnwwfHwwfHx8MA%3D%3D"
                alt="src3"
              />
              <p className="text-center text-primary">Phones</p>
            </div>
          </>
        )}
      </div>
    </>
  );
}

export default Dashboard;