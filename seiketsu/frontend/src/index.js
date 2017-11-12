import React from "react";
import ReactDOM from "react-dom";
import "./style/bulma.css";
import App from "./App";
import registerServiceWorker from "./utils/registerServiceWorker";

ReactDOM.render(<App />, document.getElementById("root"));
registerServiceWorker();