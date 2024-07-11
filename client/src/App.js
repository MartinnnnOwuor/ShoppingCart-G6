// import React from 'react'
// import './App.css'
// import Login from './component/Login'
// import Register from './component/Register'
// import Navbar from './component/Navbar'
// import Home from "./component/Home"
// import CustomersList from './component/CustomerList'
// import { BrowserRouter, Route, Routes } from 'react-router-dom'
// import About from './component/About'
// import ShoppingCart from './component/ShoppingCart'
// import Dashboard from './component/dashboard'
// function App() {
//   return (
//     <BrowserRouter>
//     <Navbar/>
//     <Routes>
//       <Route path='/' element={<Home/>} />
//       <Route path='/login' element={<Login/>}/>
//       <Route path="/register" element={<Register />} />
//       <Route path='/dashboard'element={<Dashboard/>}/>
//       <Route path='/customers' element={<CustomersList/>}/>
//       <Route path='/about' element={<About />} />
//       <Route path='/shopping' element={<ShoppingCart/>}/>
//       </Routes>
//     </BrowserRouter>
//   )
// }

// export default App


import React, { useState } from 'react';
import './App.css';
import Login from './component/Login';
import Register from './component/Register';
import Navbar from './component/Navbar';
import Home from './component/Home';
import CustomersList from './component/CustomerList';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import About from './component/About';
import ShoppingCart from './component/ShoppingCart';
import Dashboard from './component/dashboard';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const handleLogin = () => {
    setIsAuthenticated(true);
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
  };

  return (
    <BrowserRouter>
      <Navbar isAuthenticated={isAuthenticated} handleLogout={handleLogout} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login handleLogin={handleLogin} />} />
        <Route path="/register" element={<Register handleLogin={handleLogin} />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/customers" element={<CustomersList />} />
        <Route path="/about" element={<About />} />
        <Route path="/shopping" element={<ShoppingCart />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
