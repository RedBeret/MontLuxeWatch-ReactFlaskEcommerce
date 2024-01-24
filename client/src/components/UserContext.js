import React, { createContext, useState, useContext, useEffect } from "react";

const UserContext = createContext();

export const useUserContext = () => useContext(UserContext);

export const UserWrapper = ({ children }) => {
    const [user, setUser] = useState(
        JSON.parse(localStorage.getItem("user")) || null
    );

    useEffect(() => {
        if (user) {
            localStorage.setItem("user", JSON.stringify(user));
        } else {
            localStorage.removeItem("user");
        }
    }, [user]);

    const login = async (username, password) => {
        try {
            const response = await fetch("/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password }),
            });

            if (!response.ok) {
                throw new Error("Login failed");
            }

            const userDetails = await response.json();
            if (userDetails && userDetails.user_id) {
                setUser({ ...userDetails, id: userDetails.user_id });
            }
        } catch (error) {
            console.error("Error during login:", error);
        }
    };

    // Placeholder for logout function, implementation to be added later
    const logout = () => {
        // Commented out the actual logic for now
        // setUser(null);
        // localStorage.removeItem("user");
        // Implement other logout related tasks here
        // pass;
    };
    return (
        <UserContext.Provider value={{ user, login, logout }}>
            {children}
        </UserContext.Provider>
    );
};
