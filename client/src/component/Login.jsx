import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {
  
  const nav = useNavigate();
  const [logins, setLogins] = useState({
    email: "",
    password: "",
    message: "",
  });

  async function handleLogin() {
    

    let response = await fetch(
      `https://react-server-k2ig.onrender.com/users?email=${logins.email}&password=${logins.password}`,
      { method: "GET" }
    );

    let body = await response.json();
    

    if (body.length > 0) {
      //if success
      nav("/shopping");
      setLogins({
        ...logins,
        message: <span className="text-success">Login successful</span>,
      });
    } else {
      //if  error
      setLogins({
        ...logins,
        message: (
          <span className="text-danger">
            Login Unsuccessful, please try again
          </span>
        ),
      });
    }
  }

  return (
    <div className="login">
      <h4 className="border-bottom">Log-in</h4>

      {/* Beginning of the Email */}
      <div className="form-group form row">
        <label className="col-lg-4">Email:</label>
        <input
          type="text"
          className="form-control"
          value={logins.email}
          onChange={(event) => {
            setLogins({ ...logins, email: event.target.value });
          }}
        />
      </div>
      {/* End of Email */}

      {/* Beginning of the Password */}
      <div className="form-group form row">
        <label className="col-lg-4">Password:</label>
        <input
          type="password"
          className="form-control"
          value={logins.password}
          onChange={(event) => {
            setLogins({ ...logins, password: event.target.value });
          }}
        />
      </div>
      {/* End of Password */}

      <div className="d-flex justify-content-end">
        <span className="m-3 ">{logins.message}</span>

        <button
          className="btn btn-primary m-2"
          onClick={() => {
            handleLogin();
          }}
        >
          Login
        </button>
      </div>
    </div>
  );
}

//Fires when user clicks on Login button

export default Login;
