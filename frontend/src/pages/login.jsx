import {useState} from "react";
import {Link} from "react-router-dom"
import ImagePanel from "../components/image_transition.jsx";
import {UsernameIcon, PasswordIcon} from "../components/form_icons.jsx";
import styles from "./login.module.css";

// FORM VALIDATION JS LOGIC - WIP
function getLoginErrors(username, password){ //primarily check for empty fields
    const errors = [];
    const field_errors = {};

    if (!username){
        errors.push("Username cannot be empty");
        field_errors.username = true;
    }
    if (!password){
        errors.push("Password cannot be empty");
        field_errors.password = true;
    }
    
    return {errors, field_errors};
}

//LOGIN PAGE
export default function Login() {
    const [form_data, setFormData] = useState({
        username: "",
        password: "",
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

        const {username, password} = form_data;
        const {errors, field_errors: new_field_errors} = getLoginErrors(username, password)

        if (errors.length > 0){
        setErrorMessage(errors.join("\n"));
        setFieldErrors(new_field_errors);
        return;
        }
    

        // FLASK CALL
        setIsSubmitting(true);
        setErrorMessage(""); //should only happen assuming errors are clear

        try {
            const response = await fetch("http://localhost:5000/api/login", { //WIP: PLACEHOLDER LINK
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({username, password}),
            });

            const data = await response.json();
            if (!response.ok){ //flask error
                setErrorMessage(data.error || "Could not process login. Please retry.");
            }
            else {
                console.log("Successful login: ", data);
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
        <div className = {styles.login_container}>
            <ImagePanel style_class = {styles.image_panel} />

            <div className = {styles.form_panel}>
                <h1>Log In</h1>
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

                <button type = "submit" disabled = {is_submitting}>
                    {is_submitting ? "Logging In..." : "Log In"}
                </button>

                <p>
                    Not a member? <Link to = "/signup">Sign up here.</Link>
                </p>

                </form>
            </div>
        </div>
    );
}