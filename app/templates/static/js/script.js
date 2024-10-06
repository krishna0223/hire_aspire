// script.js

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Example of a simple alert for form submission
document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent default form submission
    alert('Form submitted successfully!'); // Display an alert
    // Here you can add your form submission logic (e.g., AJAX request)
});
