import React from 'react';
import { Link } from 'react-router-dom';

function Welcome() {
  return (
    <div className="welcome">
      <h1>Welcome to e-Kart</h1>
      <p>Your one-stop shop for all your needs!</p>
      <Link to="/login">
        <button className="btn btn-primary">Login</button>
      </Link>
    </div>
  );
}

export default Welcome;
