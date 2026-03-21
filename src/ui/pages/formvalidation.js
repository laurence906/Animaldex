const form = document.getElementById("form");

const username_input = document.getElementById("username_input");
const email_input = document.getElementById("email_input");
const password_input = document.getElementById("password_input");
const verify_password_input = document.getElementById("verify_password_input");
const error_message = document.getElementById("error_message");

form.addEventListener("submit", (e) => {
    
    let errors = [];

    if (email_input){ //signup
        errors = getSignupError(username_input.value, 
            email_input.value, password_input.value, 
            verify_password_input.value)
    }
    else{ //login
        errors = getLoginError(username_input.value, password_input.value)
    }

    if (errors.length > 0){
        e.preventDefault();
        error_message.innerText = errors.join("\n");
    }
})

function getSignupError(username, email, password, verify_password){
    let errors =  [];
    if (username === "" || username == null){
        errors.push("Username cannot be empty");    
        username_input.parentElement.classList.add("incorrect");
    }
    if (email === "" || email == null){
        errors.push("Email cannot be empty");
        email_input.parentElement.classList.add("incorrect");
        // TODO: validation for email format
    }
    if (password === "" || password == null){
        errors.push("Password cannot be empty");
        password_input.parentElement.classList.add("incorrect");
    }
    if (password !== verify_password){
        errors.push("Passwords do not match");
        password_input.parentElement.classList.add("incorrect");
        verify_password_input.parentElement.classList.add("incorrect");
    }
    
    return errors;
}

function getLoginError(username, password){
    let errors = [];

    if (username === "" || username == null){
        errors.push("Username cannot be empty");    
        username_input.parentElement.classList.add("incorrect");
    }
    if (password === "" || password == null){
        errors.push("Password cannot be empty");
        password_input.parentElement.classList.add("incorrect");
    }

    return errors;
}

const inputs = [username_input, email_input, password_input, verify_password_input].filter(jnput => input != null);

inputs.forEach(input => {
    input.addEventListener("input", () => {
        if(input.parentElement.classList.contains("incorrect")){
            input.parentElement.classList.remove("incorrect");
        }
    })
})