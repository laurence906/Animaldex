const images = ["../elements/heron.jpg", "../elements/fruitbat.jpg", "../elements/brownbear.jpg"]; //set all images in array

let current_img = 0;
const panel = document.querySelector(".image-panel");

setInterval(() => { //change image CSS
    current_img = (current_img + 1) % images.length;
    const next_img = document.createElement("div");

    next_img.style.cssText = `
        position: absolute;
        inset: 0;
        background-image: url("${images[current_img]}");
        background-size: cover;
        background-position: center;
        opacity: 0;
        transition: opacity 2s ease-in-out;
        z-index: 0;
    `;

    panel.appendChild(next_img); //add new image layer
    requestAnimationFrame(() => { //update before transition
        requestAnimationFrame(() => next_img.style.opacity = 1);
    });

    setTimeout(() => { //cycle layers / remove old
        while (panel.children.length > 1){
            panel.removeChild(panel.firstChild);
        }
    }, 2100); //offset for transition time (ms)
}, 8000) //time between changes (ms)