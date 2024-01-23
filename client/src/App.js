// App.js
import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "./pages/Home";
import Footer from "./components/Footer";
import NavbarMenu from "./components/NavbarMenu";

export { Home };

function App() {
  return (
    <Router>
      <NavbarMenu />
      <Switch>
        <Route exact path="/" component={Home} />
      </Switch>
      <Footer />
    </Router>
  );
}

export default App;
