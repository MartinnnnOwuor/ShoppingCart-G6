// import React from 'react'
// import { NavLink } from 'react-router-dom'

// function Navbar() {
//   return (
//     <>
//       <nav className="navbar navbar-expand-lg navbar-dark bg-dark navbar-style ">
//         <div className="container-fluid">
//         <a className="navbar-brand" href="/#">
//           #e-Kart
//         </a>

//         <button
//           className="navbar-toggler"
//           type="button"
//           data-bs-toggle="collapse"
//           data-bs-target="#navbarSupportedContent"
//           aria-controls="navbarSupportedContent"
//           aria-expanded="false"
//           aria-label="Toggle navigation"
//         >
//       <span className="navbar-toggler-icon"></span>
//         </button>

//         <div className="collapse navbar-collapse" id="navbarSupportedContent">
//           <ul className="navbar-nav me-auto mb-2 mb-lg-0">
//             <li className="nav-item">
//                 <NavLink class='home' to='/home' style={{color:'white', textDecoration:'none', marginLeft:'700px'}}>
//                   Home
//                 </NavLink>
//             </li>
//             <li  className="nav-item">
//               <NavLink class='about' style={{color:'white',textDecoration:'none',marginLeft:'50px'}} to='/about'>About</NavLink>
//             </li>
//             <li className="nav-item">
//               <NavLink style={{color:'white', textDecoration:'none',marginLeft:'50px'}} to='/dashboard'>Dashboard</NavLink>
//             </li>
//             <li  className="nav-item">
//               <NavLink class='log' style={{color:'white',textDecoration:'none',marginLeft:'50px'}} to='/'>Login</NavLink>
//             </li>
//             <li className="nav-item">
//               <NavLink class='list' style={{color:'white', textDecoration:'none',marginLeft:'50px'}} to='/customers'>Customers List</NavLink>
//             </li>
//           </ul>
//         </div>
//       </div>
//     </nav>
//   </>
//   )
// }

// export default Navbar



// import React from 'react';
// import { NavLink } from 'react-router-dom';

// function Navbar() {
//   return (
//     <>
//       <nav className="navbar navbar-expand-lg navbar-dark bg-dark navbar-style">
//         <div className="container-fluid">
//           <a className="navbar-brand" href="/#">
//             #e-Kart
//           </a>

//           <button
//             className="navbar-toggler"
//             type="button"
//             data-bs-toggle="collapse"
//             data-bs-target="#navbarSupportedContent"
//             aria-controls="navbarSupportedContent"
//             aria-expanded="false"
//             aria-label="Toggle navigation"
//           >
//             <span className="navbar-toggler-icon"></span>
//           </button>

//           <div className="collapse navbar-collapse" id="navbarSupportedContent">
//             <ul className="navbar-nav me-auto mb-2 mb-lg-0">
//               <li className="nav-item">
//                 <NavLink className='home' to='/' style={{color:'white', textDecoration:'none', marginLeft:'700px'}}>
//                   Home
//                 </NavLink>
//               </li>
//               <li className="nav-item">
//                 <NavLink className='about' style={{color:'white',textDecoration:'none',marginLeft:'50px'}} to='/about'>
//                   About
//                 </NavLink>
//               </li>
//               <li className="nav-item">
//                 <NavLink style={{color:'white', textDecoration:'none',marginLeft:'50px'}} to='/dashboard'>
//                   Dashboard
//                 </NavLink>
//               </li>
//               <li className="nav-item">
//                 <NavLink className='log' style={{color:'white',textDecoration:'none',marginLeft:'50px'}} to='/login'>
//                   Login
//                 </NavLink>
//               </li>
//               <li className="nav-item">
//                 <NavLink className='list' style={{color:'white', textDecoration:'none',marginLeft:'50px'}} to='/customers'>
//                   Customers List
//                 </NavLink>
//               </li>
//               <li className="nav-item">
//                 <NavLink className='register' style={{color:'white', textDecoration:'none',marginLeft:'50px'}} to='/register'>
//                   Register
//                 </NavLink>
//               </li>
//             </ul>
//           </div>
//         </div>
//       </nav>
//     </>
//   );
// }

// export default Navbar;



import React from 'react';
import { NavLink } from 'react-router-dom';

function Navbar({ isAuthenticated, handleLogout }) {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark navbar-style">
      <div className="container-fluid">
        <a className="navbar-brand" href="/#">
          #e-Kart
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <NavLink className="home" to="/" style={{ color: 'white', textDecoration: 'none', marginLeft: '700px' }}>
                Home
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="about" style={{ color: 'white', textDecoration: 'none', marginLeft: '50px' }} to="/about">
                About
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink style={{ color: 'white', textDecoration: 'none', marginLeft: '50px' }} to="/dashboard">
                Dashboard
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="list" style={{ color: 'white', textDecoration: 'none', marginLeft: '50px' }} to="/customers">
                Customers List
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="list" style={{ color: 'white', textDecoration: 'none', marginLeft: '50px' }} to="/shopping">
              Shopping Cart
              </NavLink>
            </li>
            {!isAuthenticated ? (
              <>
                <li className="nav-item">
                  <NavLink className="log" style={{ color: 'white', textDecoration: 'none', marginLeft: '50px' }} to="/login">
                    Login
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="register" style={{ color: 'white', textDecoration: 'none', marginLeft: '50px' }} to="/register">
                    Register
                  </NavLink>
                </li>
              </>
            ) : (
              <li className="nav-item">
                <button className="btn btn-link" style={{ color: 'white', textDecoration: 'none', marginLeft: '50px' }} onClick={handleLogout}>
                  Logout
                </button>
              </li>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
