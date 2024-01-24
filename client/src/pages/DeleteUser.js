import React from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import { useHistory, Link } from "react-router-dom";
import { useUserContext } from "../components/UserContext.js";

export default function DeleteUser() {
    const history = useHistory();
    const { deleteUser } = useUserContext();

    const initialValues = {
        username: "",
        password: "",
    };

    const validationSchema = Yup.object().shape({
        username: Yup.string().required("Required"),
        password: Yup.string().required("Required"),
    });

    const onSubmit = async (values, { setSubmitting, setErrors }) => {
        const { username, password } = values;

        try {
            // First, validate the user login to get the user ID
            const loginResponse = await fetch("/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password }),
            });

            if (!loginResponse.ok) {
                throw new Error("Login failed");
            }

            const { user_id } = await loginResponse.json();

            // Next, proceed to delete the user
            await deleteUser(user_id); // deleteUser should be a function in your UserContext that handles the delete operation

            alert("Account deleted successfully");
            history.push("/"); // Redirect to home or login page
        } catch (error) {
            console.error("Error during account deletion:", error);
            setErrors({ server: error.message });
        }

        setSubmitting(false);
    };

    return (
        <main className="w-full max-w-md mx-auto p-6">
            <div className="mt-7 bg-white border border-gray-200 rounded-xl shadow-sm dark:bg-gray-800 dark:border-gray-700">
                <div className="p-4 sm:p-7">
                    <div className="text-center">
                        <h1 className="block text-2xl font-bold text-gray-800 dark:text-white">
                            Login
                        </h1>
                        <p className="mt-2 text-sm text-gray-600 dark:text-gray-400">
                            Don't have an account?{" "}
                            <Link
                                to="/signup"
                                className="text-blue-600 hover:underline font-medium dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
                            >
                                Sign up here
                            </Link>
                        </p>
                    </div>

                    <Formik
                        initialValues={initialValues}
                        validationSchema={validationSchema}
                        onSubmit={onSubmit}
                    >
                        {({ isSubmitting }) => (
                            <Form className="mt-5">
                                <Field
                                    name="username"
                                    type="text"
                                    placeholder="Username"
                                    className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
                                />
                                <ErrorMessage
                                    name="username"
                                    component="div"
                                    className="text-red-500 text-xs mt-1"
                                />

                                <Field
                                    name="password"
                                    type="password"
                                    placeholder="Password"
                                    className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
                                />
                                <ErrorMessage
                                    name="password"
                                    component="div"
                                    className="text-red-500 text-xs mt-1"
                                />

                                <button
                                    type="submit"
                                    disabled={isSubmitting}
                                    className="w-full py-3 px-4 text-sm font-semibold rounded-lg bg-red-600 text-white hover:bg-red-900 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:ring-gray-600"
                                >
                                    Delete Account
                                </button>
                            </Form>
                        )}
                    </Formik>
                </div>
            </div>
        </main>
    );
}
