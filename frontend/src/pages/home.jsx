import {Link, useNavigate} from "react-router-dom";
import styles from "./home.module.css";

export default function Home() {
    const navigate = useNavigate();

    async function handleSubmit(e){ //prevent default browser behavior
        e.preventDefault();

        const file = e.target.image.files[0]; //array of files uploaded, take first
        if (!file){ //no file uploaded
            alert("No image uploaded");
            return
        }

        const form_data = new FormData(); //form data is just an image in this case
        form_data.append("image", file);
        
        try{
            const response = await fetch("http://localhost:5000/api/upload", {
                method: "POST",
                body: form_data,
            });

            const data = await response.json();
            if (!response.ok){
                console.error("Error uploading image:", data);
            }
            else{
                navigate("/dex" , {state: {imageUrl: data.imageUrl, animal: data.animal}});
                console.log("Image uploaded successfully:", data);
                // WIP: Handling image upload. Basically outputting classification, updating a user's dex, etc.
                // Increment this user's dex count
                
            }
        }
        catch (err){
            console.error("Could not upload image:", err);
        }

    }

    return (
        <div className={styles.container}>
            <h1 className={styles.title}>
                Animaldex - Submit an Image!
            </h1>

            <div className={styles.format}>

                <div className={styles.visual}>

                        <div className={styles.dex}>
                            <div className={styles.dex_hinge}></div>
                            <div className={styles.dex_body}></div>
                        </div>
                </div>

                <div className={styles.upload_container}>
                    <form onSubmit = {handleSubmit}>
                        <input
                        type="file"
                        name="image"
                        id="image_input"
                        placeholder="Upload"
                        accept="image/*"
                        />
                        <button className = {styles.submission_button} type="submit">
                            Submit Image
                        </button>
                    </form>
                </div>

            </div>    

            <div className={styles.nav_buttons}>
                <Link to = "/account">Account</Link> 
            </div>
    
        </div>
    );
}