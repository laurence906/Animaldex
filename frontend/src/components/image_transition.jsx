import {useEffect, useRef} from "react";

const images = [
    new URL("../assets/heron.jpg", import.meta.url).href,
    new URL("../assets/fruitbat.jpg", import.meta.url).href,
    new URL("../assets/brownbear.jpg", import.meta.url).href
    ];

export default function ImagePanel({style_class}) {
    const panel_ref = useRef(null);
    const current_img_ref = useRef(0);

    useEffect(() => {
        const panel = panel_ref.current;
        if (!panel) return;

        const interval = setInterval(() => {
            current_img_ref.current = (current_img_ref.current + 1) % images.length;

            //set up css for next image layer
            const next_img = document.createElement("div");
            next_img.style.cssText = `
            position: absolute;
            inset: 0;
            background-image: url("${images[current_img_ref.current]}");
            background-size: cover;
            background-position: center;
            opacity: 0;
            transition: opacity 2s ease-in-out;
            z-index: 0;
        `;
        panel.appendChild(next_img); //append next image layer

        requestAnimationFrame(() => { //update before transition
            requestAnimationFrame(() => {
                next_img.style.opacity = 1;
            });
        });

        setTimeout(() => {
            while (panel.children.length > 1) {
                panel.removeChild(panel.firstChild);
            }
        }, 2100); //offset for transition time (2000 ms + 100 ms buffer)
        }, 8000); //time between changes (8000 ms)

        return () => clearInterval(interval); //cleanup interval

    }, []);

    return <div className = {style_class} ref = {panel_ref} />;
}