import React, { createContext, useContext, useState } from "react";

// CartContext: A React context to provide a global state for the shopping cart.
const CartContext = createContext();

// useCartContext: A custom hook for easy access to the CartContext.
export const useCartContext = () => useContext(CartContext);

// CartWrapper: A component that provides the cart context to its children.
export const CartWrapper = ({ children }) => {
    // cartItems: State to store the items in the cart.
    const [cartItems, setCartItems] = useState([]);

    // removeFromCart: Function to remove an item from the cart.
    const removeFromCart = (productId) => {
        setCartItems(cartItems.filter((item) => item.id !== productId));
    };
    // updateQuantity: Function to update the quantity of a specific item in the cart.
    const updateQuantity = (productId, newQuantity) => {
        setCartItems((currentItems) => {
            return currentItems.map((item) => {
                if (item.id === productId) {
                    return { ...item, quantity: newQuantity };
                }
                return item;
            });
        });
    };
    // addToCart: Function to add a product to the cart.
    const addToCart = (product) => {
        setCartItems((currentItems) => {
            const isProductInCart = currentItems.some(
                (item) => item.id === product.id
            );
            if (isProductInCart) {
                return currentItems.map((item) =>
                    item.id === product.id
                        ? { ...item, quantity: item.quantity + 1 }
                        : item
                );
            } else {
                return [...currentItems, { ...product, quantity: 1 }];
            }
        });
    };

    // CartContext.Provider: Provides the cart context to its children components.
    return (
        <CartContext.Provider
            value={{ cartItems, addToCart, updateQuantity, removeFromCart }}
        >
            {children}
        </CartContext.Provider>
    );
};
