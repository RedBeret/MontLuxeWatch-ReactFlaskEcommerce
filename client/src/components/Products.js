import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function Products() {
    const [products, setProducts] = useState([]);
    const [setError] = useState(null);

    useEffect(() => {
        async function fetchProducts() {
            try {
                const response = await fetch("/products");
                if (!response.ok) {
                    throw new Error("Error fetching products");
                }
                const data = await response.json();
                if (data && data.products) {
                    setProducts(data.products);
                }
            } catch (error) {
                console.error("Error fetching products:", error);
                setError("Error fetching products");
            }
        }

        fetchProducts();
    }, []);

    return (
        <div className="bg-white">
            <div className="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
                <h2 className="sr-only">Products</h2>
                <div className="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 xl:gap-x-8">
                    {products.map((product) => {
                        // Format the product price
                        const formattedPrice = `$${product.price.toFixed(2)}`;

                        return (
                            <Link
                                key={product.id}
                                to={`/viewproduct/${product.id}`}
                                className="group"
                            >
                                <div className="aspect-w-1 aspect-h-1 w-full overflow-hidden rounded-lg bg-gray-200 xl:aspect-w-7 xl:aspect-h-8">
                                    <img
                                        src={`/assets/${product.image_url}`}
                                        alt={product.imageAlt}
                                        className="h-full w-full object-cover object-center group-hover:opacity-75"
                                    />
                                </div>
                                <h3 className="mt-4 text-sm text-gray-700">
                                    {product.name}
                                </h3>
                                {/* Display the formatted price */}
                                <p className="mt-1 text-lg font-medium text-gray-900">
                                    {formattedPrice}
                                </p>
                            </Link>
                        );
                    })}
                </div>
            </div>
        </div>
    );
}
