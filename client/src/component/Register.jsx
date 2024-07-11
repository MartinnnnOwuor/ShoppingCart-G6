

import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

function Register() {
  const nav = useNavigate();
  const [registerInfo, setRegisterInfo] = useState({
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
    message: "",
  });

  function validateEmail(email) {
    const re = /\S+@\S+\.\S+/;
    return re.test(email);
  }

  async function handleRegister() {
    if (!validateEmail(registerInfo.email)) {
      setRegisterInfo({
        ...registerInfo,
        message: (
          <span className="text-danger">Invalid email format</span>
        ),
      });
      return;
    }

    if (registerInfo.password !== registerInfo.confirmPassword) {
      setRegisterInfo({
        ...registerInfo,
        message: (
          <span className="text-danger">Passwords do not match</span>
        ),
      });
      return;
    }

    try {
      let response = await fetch(
        `http://localhost:5000/register`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: registerInfo.username,
            email: registerInfo.email,
            password: registerInfo.password,
          }),
        }
      );

      if (response.ok) {
        // Registration successful
        nav("/shopping");
        setRegisterInfo({
          ...registerInfo,
          message: <span className="text-success">Registration successful</span>,
        });
      } else {
        // Registration failed
        setRegisterInfo({
          ...registerInfo,
          message: (
            <span className="text-danger">
              Registration failed, please try again
            </span>
          ),
        });
      }
    } catch (error) {
      setRegisterInfo({
        ...registerInfo,
        message: (
          <span className="text-danger">Server error, please try again later</span>
        ),
      });
    }
  }

  return (
    <div className="register">
      <h4 className="border-bottom">Register</h4>

      {/* Beginning of the Username */}
      <div className="form-group form row">
        <label className="col-lg-4">Username:</label>
        <input
          type="text"
          className="form-control"
          value={registerInfo.username}
          onChange={(event) => {
            setRegisterInfo({ ...registerInfo, username: event.target.value });
          }}
        />
      </div>
      {/* End of Username */}

      {/* Beginning of the Email */}
      <div className="form-group form row">
        <label className="col-lg-4">Email:</label>
        <input
          type="text"
          className="form-control"
          value={registerInfo.email}
          onChange={(event) => {
            setRegisterInfo({ ...registerInfo, email: event.target.value });
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
          value={registerInfo.password}
          onChange={(event) => {
            setRegisterInfo({ ...registerInfo, password: event.target.value });
          }}
        />
      </div>
      {/* End of Password */}

      {/* Confirm Password */}
      <div className="form-group form row">
        <label className="col-lg-4">Confirm Password:</label>
        <input
          type="password"
          className="form-control"
          value={registerInfo.confirmPassword}
          onChange={(event) => {
            setRegisterInfo({
              ...registerInfo,
              confirmPassword: event.target.value,
            });
          }}
        />
      </div>
      {/* End of Confirm Password */}

      <div className="d-flex justify-content-end">
        <span className="m-3 ">{registerInfo.message}</span>

        <button
          className="btn btn-primary m-2"
          onClick={handleRegister}
        >
          Register
        </button>
      </div>

      <div className="text-center">
        <p>
          Already have an account? <Link to="/login">Login here</Link>
        </p>
      </div>
    </div>
  );
}

export default Register;
