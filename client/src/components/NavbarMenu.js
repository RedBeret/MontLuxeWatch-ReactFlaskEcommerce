import { Fragment, useState, useEffect } from "react";
import { Dialog, Tab, Transition } from "@headlessui/react";
import ShoppingCart from "./ShoppingCart";
import { Link } from "react-router-dom";
import {
  Bars3Icon,
  MagnifyingGlassIcon,
  ShoppingBagIcon,
  XMarkIcon,
} from "@heroicons/react/24/outline";
import logos from "../assets/img/Montluxewatchlogo.png";

const navigation = {
  categories: [
    {
      id: "Main",
      name: "Main",
      featured: [
        {
          name: "New Arrivals",
          href: "#",
          imageSrc:
            "https://tailwindui.com/img/ecommerce-images/mega-menu-category-01.jpg",
          imageAlt:
            "Models sitting back to back, wearing Basic Tee in black and bone.",
        },
        {
          name: "Basic Tees",
          href: "#",
          imageSrc:
            "https://tailwindui.com/img/ecommerce-images/mega-menu-category-02.jpg",
          imageAlt:
            "Close up of Basic Tee fall bundle with off-white, ochre, olive, and black tees.",
        },
      ],
      sections: [
        {
          id: "watches",
          name: "watches",
          items: [
            { name: "Watches", href: "#" },
            { name: "Wallets", href: "#" },
          ],
        },
        {
          id: "straps",
          name: "straps",
          items: [
            { name: "Full Nelson", href: "#" },
            { name: "My Way", href: "#" },
          ],
        },
      ],
    },
    {
      id: "New Releases",
      name: "New Releases",
      featured: [
        {
          name: "New Arrivals",
          href: "#",
          imageSrc:
            "https://tailwindui.com/img/ecommerce-images/mega-menu-category-01.jpg",
          imageAlt:
            "Models sitting back to back, wearing Basic Tee in black and bone.",
        },
        {
          name: "Basic Tees",
          href: "#",
          imageSrc:
            "https://tailwindui.com/img/ecommerce-images/mega-menu-category-02.jpg",
          imageAlt:
            "Close up of Basic Tee fall bundle with off-white, ochre, olive, and black tees.",
        },
      ],
      sections: [
        {
          id: "watches",
          name: "watches",
          items: [
            { name: "Watches", href: "#" },
            { name: "Wallets", href: "#" },
          ],
        },
        {
          id: "straps",
          name: "straps",
          items: [
            { name: "Full Nelson", href: "#" },
            { name: "My Way", href: "#" },
          ],
        },
      ],
    },
  ],
  pages: [
    { name: "Homepage", href: "/" },
    { name: "About", href: "/about" },
  ],
};

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

// Main component
export default function NavbarMenu() {
  const [cartOpen, setCartOpen] = useState(false);
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);

  const [open, setOpen] = useState(false);
  useEffect(() => {
    async function fetchCategories() {
      try {
        const response = await fetch("/api/categories");
        const data = await response.json();
        setCategories(data);
      } catch (error) {
        console.error("Error fetching categories:", error);
      }
    }

    fetchCategories();
  }, []);
  return (
    <div className="bg-gray-900 text-white">
      {/* Mobile menu */}
      <Transition.Root show={open} as={Fragment}>
        <Dialog as="div" className="relative z-40 lg:hidden" onClose={setOpen}>
          <Transition.Child
            as={Fragment}
            enter="transition-opacity ease-linear duration-300"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="transition-opacity ease-linear duration-300"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <div className="fixed inset-0 bg-black bg-opacity-25" />
          </Transition.Child>

          <div className="fixed inset-0 z-40 flex">
            <Transition.Child
              as={Fragment}
              enter="transition ease-in-out duration-300 transform"
              enterFrom="-translate-x-full"
              enterTo="translate-x-0"
              leave="transition ease-in-out duration-300 transform"
              leaveFrom="translate-x-0"
              leaveTo="-translate-x-full"
            >
              <Dialog.Panel className="relative flex w-full max-w-xs flex-col overflow-y-auto bg-black pb-12 shadow-xl">
                <div className="flex px-4 pb-2 pt-5">
                  <button
                    type="button"
                    className="relative -m-2 inline-flex items-center justify-center rounded-md p-2 text-gray-400"
                    onClick={() => setOpen(false)}
                  >
                    <span className="absolute -inset-0.5" />
                    <span className="sr-only">Close menu</span>
                    <XMarkIcon className="h-6 w-6" aria-hidden="true" />
                  </button>
                </div>
                <div className="space-y-6 border-t border-gray-200 px-4 py-6">
                  {navigation.pages.map((page) => (
                    <div key={page.name} className="flow-root">
                      <a
                        href={page.href}
                        className="-m-2 block p-2 font-medium text-white"
                      >
                        {page.name}
                      </a>
                    </div>
                  ))}
                </div>
                {/* Links */}
                <Tab.Group as="div" className="mt-2">
                  <div className="border-b border-gray-200">
                    <Tab.List className="-mb-px flex space-x-8 px-4">
                      {navigation.categories.map((category) => (
                        <Tab
                          key={category.name}
                          className={({ selected }) =>
                            classNames(
                              selected
                                ? "border-indigo-600 text-indigo-600"
                                : "border-transparent text-white",
                              "flex-1 whitespace-nowrap border-b-2 px-1 py-4 text-base font-medium"
                            )
                          }
                        >
                          {category.name}
                        </Tab>
                      ))}
                    </Tab.List>
                  </div>
                  <Tab.Panels as={Fragment}>
                    {categories.map((category) => (
                      <Tab.Panel
                        key={category.id}
                        className="space-y-10 px-4 pb-8 pt-10"
                      >
                        <div className="grid grid-cols-2 gap-x-4">
                          {category.featured.map((item) => (
                            <div
                              key={item.name}
                              className="group relative text-sm"
                            >
                              <div className="aspect-h-1 aspect-w-1 overflow-hidden rounded-lg bg-gray-100 group-hover:opacity-75">
                                <img
                                  src={item.imageSrc}
                                  alt={item.imageAlt}
                                  className="object-cover object-center"
                                />
                              </div>
                              <a
                                href={item.href}
                                className="mt-6 block font-medium text-white"
                              >
                                <span
                                  className="absolute inset-0 z-10"
                                  aria-hidden="true"
                                />
                                {item.name}
                              </a>
                              <p aria-hidden="true" className="mt-1">
                                Shop now
                              </p>
                            </div>
                          ))}
                        </div>
                        {category.sections.map((section) => (
                          <div key={section.name}>
                            <p
                              id={`${category.id}-${section.id}-heading-mobile`}
                              className="font-medium text-white"
                            >
                              {section.name}
                            </p>
                            <ul
                              aria-labelledby={`${category.id}-${section.id}-heading-mobile`}
                              className="mt-6 flex flex-col space-y-6"
                            >
                              {section.items.map((item) => (
                                <li key={item.name} className="flow-root">
                                  <a
                                    href={item.href}
                                    className="-m-2 block p-2 text-gray-500"
                                  >
                                    {item.name}
                                  </a>
                                </li>
                              ))}
                            </ul>
                          </div>
                        ))}
                      </Tab.Panel>
                    ))}
                  </Tab.Panels>
                </Tab.Group>

                <div className="space-y-6 border-t border-gray-200 px-4 py-6">
                  <div className="flow-root">
                    <button
                      className="-m-2 block p-2 font-medium text-white"
                      onClick={() => {
                        /* handle sign in logic */
                      }}
                    >
                      Sign in
                    </button>
                  </div>
                  <div className="flow-root">
                    <button
                      className="-m-2 block p-2 font-medium text-white"
                      onClick={() => {
                        /* handle create account logic */
                      }}
                    >
                      Create account
                    </button>
                  </div>
                </div>
              </Dialog.Panel>
            </Transition.Child>
          </div>
        </Dialog>
      </Transition.Root>

      <header className="relative bg-gray-900">
        <p className="flex h-10 items-center justify-center bg-indigo-600 px-4 text-sm font-medium text-white sm:px-6 lg:px-8">
          Get free delivery on orders over $100
        </p>

        {/* Main navigation */}
        <nav
          aria-label="Top"
          className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8"
        >
          <div className="border-b border-gray-700">
            {" "}
            {/* Darker border color */}
            <div className="flex h-16 items-center">
              {/* Mobile menu button */}
              <button
                type="button"
                className="relative rounded-md bg-black p-2 text-gray-400 lg:hidden"
                onClick={() => setOpen(true)}
              >
                <span className="absolute -inset-0.5" />
                <span className="sr-only">Open menu</span>
                <Bars3Icon className="h-6 w-6" aria-hidden="true" />
              </button>

              {/* Logo */}
              <div className="ml-4 flex lg:ml-0">
                <span className="sr-only">Mont Luxe Watch Company</span>
                <img
                  className="h-8 w-auto"
                  src={logos}
                  alt="Mont Luxe Watch Company logo"
                />
                <span className="ml-2 text-xl font-semibold">
                  Mont Luxe Watch Company
                </span>
              </div>

              {/* Desktop menu - Just the Homepage link */}
              <div className="hidden lg:ml-8 lg:flex lg:space-x-8">
                <Link
                  to="/"
                  className="flex items-center text-sm font-medium text-white hover:text-gray-300"
                >
                  Home
                </Link>
                <Link
                  to="/about"
                  className="flex items-center text-sm font-medium text-white hover:text-gray-300"
                >
                  About
                </Link>
              </div>

              <div className="ml-auto flex items-center">
                {/* Sign in and Create account links */}
                <div className="hidden lg:flex lg:flex-1 lg:items-center lg:justify-end lg:space-x-6">
                  <Link
                    to="/auth"
                    className="text-sm font-medium text-white hover:text-gray-300"
                  >
                    Sign in
                  </Link>
                  <span className="h-6 w-px bg-gray-600" aria-hidden="true" />
                  <Link
                    to="/signup"
                    className="text-sm font-medium text-white hover:text-gray-300"
                  >
                    Create account
                  </Link>
                </div>

                {/* Search */}
                <div className="flex lg:ml-6">
                  <a href="#" className="p-2 text-gray-300 hover:text-white">
                    {" "}
                    {/* Light text and hover effect */}
                    <span className="sr-only">Search</span>
                    <MagnifyingGlassIcon
                      className="h-6 w-6"
                      aria-hidden="true"
                    />
                  </a>
                </div>

                {/* Cart Icon */}
                <div className="ml-4 flow-root lg:ml-6">
                  <a
                    href="#"
                    className="group -m-2 flex items-center p-2"
                    onClick={(e) => {
                      e.preventDefault(); // Prevent default link behavior
                      setCartOpen(!cartOpen); // Toggle the cart open state
                    }}
                  >
                    <ShoppingBagIcon
                      className="h-6 w-6 flex-shrink-0 text-gray-300 group-hover:text-white"
                      aria-hidden="true"
                    />
                    <span className="ml-2 text-sm font-medium text-white group-hover:text-gray-300">
                      {products.length} {/* Number of items in cart */}
                    </span>
                    <span className="sr-only">items in cart, view bag</span>
                  </a>
                </div>

                {/* ShoppingCart Component */}
                {cartOpen && (
                  <ShoppingCart
                    open={cartOpen}
                    setOpen={setCartOpen}
                    products={products}
                  />
                )}
              </div>
            </div>
          </div>
        </nav>
      </header>
    </div>
  );
}
