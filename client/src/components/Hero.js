import React, { useState } from "react";
import heroImage from "../assets/img/Hero.png";

export default function Hero() {
    const [imageLoaded, setImageLoaded] = useState(false);
    return (
        <div className="relative bg-gray-300 text-white h-screen">
            {!imageLoaded && (
                <div className="absolute inset-0 bg-gray-200 animate-pulse"></div>
            )}
            <img
                src={heroImage}
                alt="Featured Watch"
                className={`w-full h-full object-cover transition-opacity duration-500 ${
                    imageLoaded ? "opacity-100" : "opacity-0"
                }`}
                onLoad={() => setImageLoaded(true)}
            />
            <div className="absolute left-0 top-1/2 transform -translate-y-1/2 text-left p-12">
                <h1 className="text-4xl mb-4 font-bold text-shadow-default shadow-lg">
                    BECAUSE YOU ARE WORTH IT
                </h1>
                <p className="mb-6 text-shadow-default shadow-lg">
                    Limited quantities available.
                </p>
                <button className="px-6 py-2 bg-orange-500 rounded-full font-bold shadow-lg hover:bg-orange-600 text-shadow">
                    GET YOURS →
                </button>
            </div>
        </div>
    );
}
