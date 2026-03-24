import {useState} from "react";
import {Link} from "react-router-dom"
import ImagePanel from "../components/image_transition.jsx";
import {UsernameIcon, EmailIcon, PasswordIcon} from "../components/form_icons.jsx";
import styles from "./signup.module.css";

// FORM VALIDATION JS LOGIC - WIP
function getSignupErrors(username, email, password, verify_password){ //primarily check for empty fields
    const errors = [];
    const field_errors = {};

    if (!username){
        errors.push("Username cannot be empty");
        field_errors.username = true;
    }
    if (!email){
        errors.push("Email cannot be empty");
        field_errors.email = true;
    }
    if (!password){
        errors.push("Password cannot be empty");
        field_errors.password = true;
    }
    if (password !== verify_password){
        errors.push("Passwords do not match");
        field_errors.verify_password = true;
    }
    
    return {errors, field_errors};
}

//SIGNUP PAGE
export default function Signup() {
    const [form_data, setFormData] = useState({
        username: "",
        email: "",
        password: "",
        verify_password: ""
    });

    //setup vars
    const [error_message, setErrorMessage] = useState("");
    const [field_errors, setFieldErrors] = useState({});
    const [is_submitting, setIsSubmitting] = useState(false);

    function handleChange(e) { //event handling
        const {name, value} = e.target;
        setFormData((prev) => ({ ...prev, [name]: value }));
        
        if (field_errors[name]){ //reset error if user rewrites in field
            setFieldErrors((prev => ({...prev, [name]: false})))
        }
    }

    async function handleSubmit(e) { //submission made
        e.preventDefault();

        const {username, email, password, verify_password} = form_data;
        const {errors, field_errors: new_field_errors} = getSignupErrors(username, email, password, verify_password)

        if (errors.length > 0){
        setErrorMessage(errors.join("\n"));
        setFieldErrors(new_field_errors);
        return;
        }
    

        // FLASK CALL
        setIsSubmitting(true);
        setErrorMessage(""); //should only happen assuming errors are clear

        try {
            const response = await fetch("http://localhost:5000/api/signup", { //WIP: PLACEHOLDER LINK
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({username, email, password}),
            });

            const data = await response.json();
            if (!response.ok){ //flask error
                setErrorMessage(data.error || "Could not process signup. Please retry.");
            }
            else {
                console.log("Successful signup: ", data);
                //WIP: navigate to next page
            }
        }
        catch (err) {
            setErrorMessage("Could not connect. Please retry");
        }
        finally {
            setIsSubmitting(false);
        }
    }

    //USER INTERFACE / HTML
    return (
        <div className = {styles.signup_container}>
            <ImagePanel style_class = {styles.image_panel} />

            <div className = {styles.form_panel}>
                <h1>Sign Up</h1>
                {error_message && (
                    <p className = {styles.error_message}>{error_message}</p>
                )}

                <form onSubmit = {handleSubmit} noValidate>
                <div className = {field_errors.username ? styles.incorrect : ""}>
                    <label htmlFor="username_input">
                        <UsernameIcon />
                    </label>
                    <input
                        type = "text"
                        id = "username_input"
                        name = "username"
                        placeholder = "Username"
                        value = {form_data.username}
                        onChange = {handleChange}
                    />
                </div>

                <div className = {field_errors.email ? styles.incorrect : ""}>
                    <label htmlFor="email_input">
                        <EmailIcon />
                    </label>
                    <input
                        type = "text"
                        id = "email_input"
                        name = "email"
                        placeholder = "Email"
                        value = {form_data.email}
                        onChange = {handleChange}
                    />
                </div>

                <div className = {field_errors.password ? styles.incorrect : ""}>
                    <label htmlFor="password_input">
                        <PasswordIcon />
                    </label>
                    <input
                        type = "text"
                        id = "password_input"
                        name = "password"
                        placeholder = "Password"
                        value = {form_data.password}
                        onChange = {handleChange}
                    />
                </div>

                <div className = {field_errors.verify_password ? styles.incorrect : ""}>
                    <label htmlFor="verify_password_input">
                        <PasswordIcon />
                    </label>
                    <input
                        type = "text"
                        id = "verify_password_input"
                        name = "verify_password"
                        placeholder = "Verify Password"
                        value = {form_data.verify_password}
                        onChange = {handleChange}
                    />
                </div>

                <button type = "submit" disabled = {is_submitting}>
                    {is_submitting ? "Signing Up..." : "Sign Up"}
                </button>

                <p>
                    Already a member? <Link to = "/login">Log in here.</Link>
                </p>

                </form>
            </div>
        </div>
    );
}