import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "./pages/Home";
import Footer from "./components/Footer";
import NavbarMenu from "./components/NavbarMenu";
import ViewProduct from "./pages/ViewProduct";
import About from "./pages/About";
import Checkout from "./pages/Checkout";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import { CartWrapper } from "./components/CartContext";
import DeleteUser from "./pages/DeleteUser";
import UpdatePassword from "./pages/UpdatePassword";
import Contact from "./pages/Contact";

function App() {
    return (
        <CartWrapper>
            <Router>
                <NavbarMenu />
                <Switch>
                    <Route exact path="/" component={Home} />
                    <Route path="/about" component={About} />
                    <Route path="/checkout" component={Checkout} />
                    <Route path="/login" component={Login} />
                    <Route path="/signup" component={Signup} />
                    <Route path="/deleteuser" component={DeleteUser} />
                    <Route path="/UpdatePassword" component={UpdatePassword} />
                    <Route path="/viewproduct/:id" component={ViewProduct} />
                    <Route path="/contact" component={Contact} />
                </Switch>
                <Footer />
            </Router>
        </CartWrapper>
    );
}

export default App;
