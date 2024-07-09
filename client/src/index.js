import React from "react";
import { createRoot } from "react-dom/client";
import "jquery";
import "popper.js/dist/umd/popper";
import "bootstrap/dist/js/bootstrap";
import "bootstrap/dist/css/bootstrap.css";
import "./App.css";
import App from "./App";
import "@fortawesome/fontawesome-free/css/all.css";

const element = <App />;
const root = createRoot(document.getElementById("root"));
root.render(element);
// console.log (element);