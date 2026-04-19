import {Link, useNavigate} from "react-router-dom";
import styles from "./accountinfo.module.css";

export default function AccountInfo() {
    const navigate = useNavigate();
    /*
    WIP: need to implement:
    - logout features
    - dex tracking features
    - both as items in DB
    */

    return (
    <div className = {styles.container}>
            <h1 className = {styles.title}>Account Info</h1>
        
            <div className = {styles.infoContainer} id = "user-container">
                <h2 id = "username">Username:</h2>
                <p id = "email">Email:</p>
                <p id= "dex_num">Your total number of dex entries is: </p>
            </div>

            <div className = {styles.navButtons}>
                <button id= "logout_button" onClick={() => navigate('/login')}>Logout</button>
                <button id= "home_button" onClick={() => navigate('/home')}>Home</button>
            </div>

    </div>
    );
}