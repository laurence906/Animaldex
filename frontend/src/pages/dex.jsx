import { useLocation, Link } from "react-router-dom";
import styles from "./dex.module.css";

export default function Dex() {
    const { state } = useLocation();
    if (!state){
        return <div>No data available</div>
    }
    const { modelResult } = state || {};

    if (!modelResult) {
        return <div>No model result available</div>
    }

    // Parse the taxonomyPath in modelResult.
    const parts = modelResult[0].split(';');
    let animal = parts[parts.length - 1];

    if (animal === "blank"){
        animal = "nothing";
    }

    // Format the species name for display and Wikipedia search.
    const animalURL = animal.replace(/_/g, ' '); // Replace underscores with spaces for display.

    // Format animal to be capitalized
    let animalDisplay = animalURL.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
    

    return (
        <div className={styles.container}>

            <h1 className={styles.title}>
                Your Animal Is:
            </h1>

            <div className={styles.open_dex}>

                <div className={styles.left_panel}>

                    <div className={`${styles.screen} ${styles.left_text_screen}`}>
                        <p className={styles.congrats}>Congratulations!</p>
                        <p className={styles.found}>You found:</p>
                        <p className={styles.species}>{animalDisplay}</p>
                        {/* <img className={styles.animal_image} src={} alt="Uploaded Animal"/> */}
                    </div>

                </div>

                <div className={styles.hinge}></div>

                <div className={styles.right_panel}>

                    <div className={`${styles.screen} ${styles.animal_info}`}>
                        <iframe src={`https://en.wikipedia.org/wiki/${animalURL}`} title= "Wikipedia" className= {styles.wiki_frame}/>
                    </div>

                </div>

            </div>

            <div className={styles.nav_buttons}>
                <Link to="/account">Account</Link>
                <Link to="/home">Return</Link>
            </div>

        </div>
    );
}