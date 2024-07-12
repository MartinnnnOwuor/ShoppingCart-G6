import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {
  const nav = useNavigate();
  const [logins, setLogins] = useState({
    username: "",
    password: "",
    message: "",
  });

  const [registers, setRegisters] = useState({
    username: "",
    password: "",
    message: "",
  });

  async function handleLogin() {
    try {
      let response = await fetch("http://localhost:5000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: logins.username,
          password: logins.password,
        }),
      });
  
      let body = await response.json();
  
      if (response.status === 200) {
        localStorage.setItem("token", body.access_token);
        nav("/dashboard");
        setLogins({
          ...logins,
          message: <span className="text-success">Login successful</span>,
        });
      } else {
        setLogins({
          ...logins,
          message: (
            <span className="text-danger">
              Login Unsuccessful, please try again
            </span>
          ),
        });
      }
    } catch (error) {
      console.error("Error logging in:", error);
    }
  }
  
  async function handleRegister() {
    try {
      let response = await fetch("http://localhost:5000/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: registers.username,
          password: registers.password,
        }),
      });
  
      let body = await response.json();
  
      if (response.status === 201) {
        setRegisters({
          ...registers,
          message: <span className="text-success">Registration successful</span>,
        });
      } else {
        setRegisters({
          ...registers,
          message: (
            <span className="text-danger">
              Registration Unsuccessful, please try again
            </span>
          ),
        });
      }
    } catch (error) {
      console.error("Error registering:", error);
    }
  }

  return (
    <div className="login">
      <h4 className="border-bottom">Log-in</h4>
      <div className="form-group form row">
        <label className="col-lg-4">Username:</label>
        <input
          type="text"
          className="form-control"
          value={logins.username}
          onChange={(event) => {
            setLogins({ ...logins, username: event.target.value });
          }}
        />
      </div>
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

      <h4 className="border-bottom">Register</h4>
      <div className="form-group form row">
        <label className="col-lg-4">Username:</label>
        <input
          type="text"
          className="form-control"
          value={registers.username}
          onChange={(event) => {
            setRegisters({ ...registers, username: event.target.value });
          }}
        />
      </div>
      <div className="form-group form row">
        <label className="col-lg-4">Password:</label>
        <input
          type="password"
          className="form-control"
          value={registers.password}
          onChange={(event) => {
            setRegisters({ ...registers, password: event.target.value });
          }}
        />
      </div>
      <div className="d-flex justify-content-end">
        <span className="m-3 ">{registers.message}</span>
        <button
          className="btn btn-primary m-2"
          onClick={() => {
            handleRegister();
          }}
        >
          Register
        </button>
      </div>
    </div>
  );
}

export default Login;
