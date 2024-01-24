import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "./pages/Home";
import Footer from "./components/Footer";
import NavbarMenu from "./components/NavbarMenu";
import ViewProduct from "./pages/ViewProduct";
import About from "./pages/About";
import Checkout from "./pages/Checkout";
// import Login from "./pages/Login";
// import Signup from "./pages/Signup";

// Add missing imports
function App() {
  return (
    <Router>
      <NavbarMenu />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
        <Route path="/checkout" component={Checkout} />

        <Route path="/viewproduct/:id" component={ViewProduct} />
      </Switch>
      <Footer />
    </Router>
  );
}

export default App;

//  <Route path="/login" component={Login} />
// <Route path="/signup" component={Signup} />
