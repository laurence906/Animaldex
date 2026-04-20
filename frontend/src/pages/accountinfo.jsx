import {useNavigate} from "react-router-dom";
import {useEffect, useState} from "react";
import styles from "./accountinfo.module.css";

export default function AccountInfo() {
    const navigate = useNavigate();
    const [user_data, setUserData] = useState({
        username: "",
        email: "",
        dex_entries: 0
    });

    const [error_message, setErrorMessage] = useState("");

    useEffect(() => {
        const token = localStorage.getItem("token");
        if (!token) {
            navigate("/login"); //go back to login if no login token is detected
            return;
        }

        async function getAccountInfo() {
            try{
                const response = await fetch("http://localhost:5000/api/account", {
                    method: "GET",
                    headers: {
                        "Authorization": `Bearer ${token}`
                    }
                });

                const data = await response.json();
                if (!response.ok) {
                    setErrorMessage(data.error || "Could not get account info.");
                }
                else{
                    setUserData(data);
                }
            }
            catch (err){
                setErrorMessage("Could not connect.")
            }
        }

        getAccountInfo();
    }, []);

    function logout(){
        localStorage.removeItem("token");
        navigate("/login");
    }
    

    return (
    <div className = {styles.container}>
        <h1 className = {styles.title}>Account Info</h1>

        {error_message && <p className = {styles.error_message}>{error_message}</p>}
        
            <div className = {styles.info_container} id = "user-container">
                <p> Username: {user_data.username} </p>
                <p> Email: {user_data.email} </p>
                <p> Total Dex Entries: {user_data.dex_entries} </p>
            </div>

            <div className = {styles.nav_buttons}>
                <button onClick = {logout}> Logout </button>
                <button onClick = {() => navigate("/home")}> Home </button>
            </div> 
    </div>
    );
}