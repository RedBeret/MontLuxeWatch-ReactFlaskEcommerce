import React from "react";

export default function Contact() {
    return (
        <div className="py-14 sm:py-14 bg-gray-100 flex flex-col justify-center items-center px-6 sm:px-12">
            <div className="bg-white shadow-lg rounded-lg p-6 sm:p-12 w-full max-w-2xl">
                <h1 className="text-2xl font-bold mb-4 text-center text-gray-800 sm:text-3xl">
                    Contact Us
                </h1>
                <div className="contact-info space-y-2 text-gray-600">
                    <p className="font-semibold text-lg">
                        Mont Luxe Watch Company
                    </p>
                    <p>1234 Watchmaker Lane</p>
                    <p>4000 Basel</p>
                    <p>Switzerland</p>
                    <p>
                        <strong>Email:</strong> contact@montluxewatchco.fake
                    </p>
                    <p>
                        <strong>Phone:</strong> +41 22 501 7070
                    </p>
                </div>
            </div>
        </div>
    );
}
