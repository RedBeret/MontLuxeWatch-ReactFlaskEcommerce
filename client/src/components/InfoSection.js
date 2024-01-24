import React from "react";

function InfoSection() {
    return (
        <div className="bg-gray-200 py-16">
            <div className="container mx-auto">
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
                    {/* Column 1 */}
                    <div className="col-span-1">
                        <h2 className="text-3xl font-bold text-gray-800 mb-4 text-center">
                            Experience Luxury Timekeeping
                        </h2>
                        <p className="text-base text-gray-600 leading-6 text-center">
                            Mont Luxe Watch Company brings you the epitome of
                            luxury timepieces. Crafted in the heart of
                            Switzerland, our watches are a testament to Swiss
                            excellence, combining rugged beauty with unmatched
                            luxury.
                        </p>
                    </div>

                    {/* Column 2 */}
                    <div className="col-span-1">
                        <h2 className="text-3xl font-bold text-gray-800 mb-4 text-center">
                            Unparalleled Craftsmanship
                        </h2>
                        <p className="text-base text-gray-600 leading-6 text-center">
                            Each Mont Luxe timepiece is meticulously crafted by
                            Swiss artisans using centuries-old techniques. Our
                            watches are not just instruments of time; they are
                            heirlooms designed to be cherished for generations.
                        </p>
                    </div>

                    {/* Column 3 */}
                    <div className="col-span-1">
                        <h2 className="text-3xl font-bold text-gray-800 mb-4 text-center">
                            Sustainable Luxury
                        </h2>
                        <p className="text-base text-gray-600 leading-6 text-center">
                            We are committed to sustainability. Mont Luxe
                            embraces eco-friendly practices in our manufacturing
                            processes, ensuring that our watches are not only a
                            symbol of elegance but also responsibility towards
                            the environment.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default InfoSection;
