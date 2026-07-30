// Set current date on the mockup
document.addEventListener('DOMContentLoaded', () => {
    const dateElement = document.getElementById('current-date');
    if (dateElement) {
        const options = { weekday: 'long', day: 'numeric', month: 'long' };
        dateElement.textContent = new Date().toLocaleDateString('pt-BR', options);
    }
});

// Scroll Reveal Animation
function reveal() {
    var reveals = document.querySelectorAll(".reveal");

    for (var i = 0; i < reveals.length; i++) {
        var windowHeight = window.innerHeight;
        var elementTop = reveals[i].getBoundingClientRect().top;
        var elementVisible = 100;

        if (elementTop < windowHeight - elementVisible) {
            reveals[i].classList.add("active");
        }
    }
}

window.addEventListener("scroll", reveal);
// Trigger once on load
reveal();

// Mockup interactive slots
const slots = document.querySelectorAll('.slot:not(.disabled)');
slots.forEach(slot => {
    slot.addEventListener('click', function() {
        // Remove active from all
        slots.forEach(s => {
            s.style.backgroundColor = '';
            s.style.color = '';
            s.style.borderColor = '';
        });
        
        // Add to clicked
        this.style.backgroundColor = 'var(--brand-green)';
        this.style.color = 'white';
        this.style.borderColor = 'var(--brand-green)';
    });
});
