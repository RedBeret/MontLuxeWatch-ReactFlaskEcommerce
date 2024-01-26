# Mont Luxe Watch Company E-Commerce Platform

## Project Overview

Disclaimer: Please note that the Mont Luxe Watch Company E-Commerce Platform is a conceptual project created for educational purposes. This store, including its products and services, does not exist in reality and has been developed as a part of a learning endeavor in full-stack web application development.

The Mont Luxe Watch Company E-Commerce Platform represents a sophisticated elegance in web application development, designed to elegantly showcase and facilitate the sale of luxury timepieces. Technologies used and learned are below, this flows up to the checkout page has CRUD on Users with bcrypt on the hashed passwords utilizing frontend and backend full stack Python, Flask, SQlite3, SQL Alchemy, React JS, and Tailwind CSS. 

Key Technologies and Features:
1. **Flask Backend**: Utilizes the Flask framework for robust server-side operations, ensuring efficient handling of HTTP requests, data processing, and API interactions.
2. **React Frontend**: Employs React to create a dynamic and responsive user interface, offering an immersive and intuitive experience for browsing and purchasing luxury watches.
3. **SQLite Database**: Implements SQLite for reliable and scalable data storage, managing product inventories, user data, and transactional information with precision.
4. **Bcrypt for Security**: Incorporates Flask-Bcrypt for advanced security measures, specifically in hashing and securing user passwords.
5. **Marshmallow for Serialization**: Utilizes Marshmallow for object serialization and deserialization, enhancing data integrity between the backend and frontend.
6. **Responsive and Elegant Design**: Tailwind CSS is integrated to provide a visually appealing, mobile-responsive design, aligning with the luxurious essence of the product line.
7. **User Authentication and Management**: Features a comprehensive user authentication system, supporting secure user registration, login, and profile management.
8. **Interactive Shopping Cart**: Implements an interactive shopping cart system, allowing users to seamlessly add items, adjust quantities, and proceed to checkout.
10. **Python Validations**: Employs Python for backend data validation, ensuring robust error handling and data integrity.

## Technology Stack

- **Frontend**: React, Tailwind CSS, Formik, Yup (for form validation).
- **Backend**: Flask, Flask-RESTful, Flask-SQLAlchemy, Flask-Migrate.
- **Database**: SQLite.
- **Version Control**: Git, GitHub
- **Testing and Debugging**: Postman, Insomnia
- **Additional Tools**: HeadlessUI, Heroicons, Faker

### Objectives and Learning Outcomes

1. **Hands-On Experience**: Gain practical experience in building a full-stack application.
2. **Technology Integration**: Learn to integrate various technologies like Flask, React, and SQLite.
3. **Database Management**: Understand the intricacies of managing a database in a dynamic website.
4. **Frontend Development**: Enhance skills in frontend development using React and various libraries.
5. **Backend Development**: Develop backend proficiency with Flask and RESTful API design.

## Key Features

- **Product Display**: Showcases luxury watches with detailed descriptions and high-quality images.
- **User Authentication**: Secure login, sign-up, and account management functionalities.
- **Shopping Cart**: Allows users to add products to a cart and manage quantities.
- **Checkout Process**: Facilitates the collection of shipping details and processes orders.
- **Responsive Design**: Ensures a seamless experience across various devices and screen sizes.

## Directory Structure

```
├── Pipfile
├── README.md
├── client
│   ├── README.md
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   ├── src
│   │   ├── App.js
│   │   ├── assets
│   │   │   └── img
│   │   ├── components
│   │   │   ├── CartContext.js
│   │   │   ├── Footer.js
│   │   │   ├── Hero.js
│   │   │   ├── InfoSection.js
│   │   │   ├── NavbarMenu.js
│   │   │   ├── Products.js
│   │   │   └── ShoppingCart.js
│   │   ├── index.css
│   │   ├── index.js
│   │   └── pages
│   │       ├── About.js
│   │       ├── Checkout.js
│   │       ├── Contact.js
│   │       ├── DeleteUser.js
│   │       ├── Home.js
│   │       ├── Login.js
│   │       ├── Signup.js
│   │       ├── UpdatePassword.js
│   │       └── ViewProduct.js
│   └── tailwind.config.js
└── server
    ├── app.py
    ├── config.py
    ├── helpers.py
    ├── migrations
    ├── models.py
    └── seed.py
```

## Lessons Learned

1. **Full-Stack Integration**: Learned how to seamlessly integrate frontend and backend components into a cohesive application.
2. **Database Handling**: Gained experience in designing and managing a database with SQLite and SQLAlchemy.
3. **User Interface Design**: Developed skills in crafting intuitive and responsive user interfaces with React and Tailwind CSS.
4. **Security and Authentication**: Implemented secure user authentication.
5. **API Development**: Created and utilized RESTful APIs for data interaction between frontend and backend.

## Future Enhancements

1. **Payment Integration and Security**: Implement a secure payment gateway with multiple payment options, and enhance user security with robust authentication and authorization features.
2. **User Experience Improvements**: Develop advanced product filtering and search capabilities, and introduce customer reviews and ratings for products.
3. **Session Persistence and Database Optimization**: Utilize cookies for persistent user sessions and optimize the database by separating user and shipping data for efficiency.
4. **Post-Checkout Process Enhancement**: Enhance user engagement with features like order confirmation, order tracking, and an accessible order history for logged-in users.

## Conclusion

The Mont Luxe Watch E-Commerce Platform is a prime example of effective web development. This project highlights key aspects:

- Full-stack development: Integrating Flask, React, and SQLite for a seamless user experience.
- Database management: Efficient handling of data for product display and transactions.
- User Interface: A focus on design and functionality, enhancing user interaction.

It's more than just an e-commerce site; it's a showcase of learning and skill application in web development. If you would like to try it follow the steps below.


# Mont Luxe Watch Company E-Commerce Platform Setup Guide

Welcome to the Mont Luxe Watch Company E-Commerce Platform. This guide will walk you through the steps to set up your development environment for both the backend (Flask) and frontend (React) components of the application.

## Preparing the Backend Environment (`server/`)
Before initializing the database, ensure you have a `.env` file set up in your `server` directory. This file will store essential environment variables for your Flask application.

### Generating the Secret Key
1. Open a terminal.
2. Generate a new secret key by running the following command:
    ```console
    python -c 'import secrets; print(secrets.token_hex())'
    ```
3. Copy the output; this is your secret key.

### Creating the .env File
1. In your `server` directory, create a file named `.env`.
2. Add the following lines to the `.env` file:
    ```
    SECRET_KEY=<Your Secret Key>
    DB_URI="sqlite:///app.db"
    ```
   Replace `<Your Secret Key>` with the key you generated.

### Installing Dependencies
After cloning the project, install backend dependencies and activate the virtual environment:
```console
pipenv install
pipenv shell
```

### Running the Flask API
To run the Flask API locally (default port 5555):
```console
python server/app.py
```

## Preparing the Frontend Environment (`client/`)
The `client/` directory contains the React frontend code.

### Installing React Dependencies
To install frontend dependencies:
```console
npm install --prefix client
```

### Starting the React App
To start the React app locally (default port 3000):
```console
npm start --prefix client
```

## Database Initialization and Seeding
After setting up your `.env` file and installing dependencies, you can initialize and seed your database. Ensure you're in the `server` directory, then run:

```sh
export FLASK_APP=app.py
export FLASK_RUN_PORT=5555

{ flask db init && echo "DB init successful"; } || echo "DB init failed, continuing..."
{ flask db migrate -m "initial migration" && echo "DB migrate successful"; } || echo "DB migrate failed, continuing..."
{ flask db upgrade head && echo "DB upgrade successful"; } || echo "DB upgrade failed, continuing..."
{ python seed.py && echo "Seeding successful"; } || echo "Seeding failed"
```

These commands will initialize the database, perform migrations, upgrade to the latest version, and seed it with initial data. After this you should see it on your http://localhost:3000/ enjoy! ☺️

