// client/src/pages/Home.js
import React from "react";
import Hero from "../components/Hero";
import InfoSection from "../components/InfoSection";
import Products from "../components/Products";

export default function Home() {
    return (
        <>
            <Hero />
            <Products />
            <InfoSection />
        </>
    );
}
