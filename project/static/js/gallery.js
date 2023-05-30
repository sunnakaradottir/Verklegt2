let slideIndex = 1;

// Function to show the current slide
function showSlides(n) {
    const slides = document.getElementsByClassName("mySlides");

    // Wrap around the slides if reaching the end
    if (n > slides.length) {
        slideIndex = 1;
    } else if (n < 1) {
        slideIndex = slides.length;
    }

    // Hide all slides
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    // Display the current slide
    slides[slideIndex - 1].style.display = "block";
}

// Function to navigate to the previous slide
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Function to navigate to a specific slide
function currentSlide(n) {
    showSlides(slideIndex = n);
}

// Show the initial slide
showSlides(slideIndex);