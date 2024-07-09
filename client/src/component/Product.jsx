import React, { useEffect } from "react";

const Product = ({ product, onDelete, onIncrement, onDecrement, children }) => {
  useEffect(() => {
    // componentDidMount logic can go here if needed
    return () => {
      // componentWillUnmount logic can go here if needed
    };
  }, []);

  return (
    <div className="col-lg-6" style={{ width: "400px", marginLeft:'70px' }}>
      <div className="card m-2" style={{background:'#ccc'}}>
        <div className="card-body">
          <div className="text-muted" >
            # {product.id}
            <span
              className="d-flex justify-content-end hand-icon"
              onClick={() => {
                onDelete(product);
              }}
            >
              <i className="fa fa-times" style={{color:'red', background:'white'}}></i>
            </span>
          </div>
          <h5 className="pt-1 border-top" style={{color:'blue'}}>{product.nameOfProduct}</h5>
          <div style={{color:'green'}}>ksh{product.price}</div>
        </div>
        <div>
          <img
            className="pt-1 border-top"
            src={product.imageUrl}
            height="240px"
            width="357px"
            alt={product.nameOfProduct}
          />
        </div>
        <div className="card-footer d-flex justify-content-between align-items-center">
          <div className="d-flex">
            <span
              className="badge"
              style={{ backgroundColor: "#0000ff", color: "#fff",marginRight:'8px',padding:'14px' }}
            >
              {product.quantity}
            </span>
            <div className="btn-group">
              <button
                className="btn btn-outline-success"
                onClick={() => {
                  onIncrement(product, 20);
                }}
              >
                +
              </button>
              <button
                className="btn btn-outline-success"
                onClick={() => {
                  onDecrement(product, 0);
                }}
              >
                -
              </button>
            </div>
          </div>
          <div>{children}</div>
        </div>
      </div>
    </div>
  );
};

export default Product;