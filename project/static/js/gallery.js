let slideIndex = 1;

function showSlides(n) {
    const slides = document.getElementsByClassName("mySlides");
    if (slides.length === 0) {
        return; // if no slides are found, exit the function to avoid errors
    }

    if (n > slides.length) {
        slideIndex = 1;
    } else if (n < 1) {
        slideIndex = slides.length;
    }

    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slides[slideIndex - 1].style.display = "flex";
}

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

showSlides(slideIndex);