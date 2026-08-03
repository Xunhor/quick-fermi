/**
 * Main JavaScript for SuaAgência
 * Handles scroll animations (Intersection Observer) and micro-interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. SCROLL REVEAL ANIMATIONS (Intersection Observer)
    const revealElements = document.querySelectorAll('[data-reveal]');
    
    const revealOptions = {
        threshold: 0.15, // Trigger when 15% of the element is visible
        rootMargin: "0px 0px -50px 0px" // Trigger slightly before it hits the bottom
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Get delay if specified in HTML (e.g., data-delay="200")
                const delay = entry.target.getAttribute('data-delay') || 0;
                
                setTimeout(() => {
                    entry.target.classList.add('is-visible');
                }, delay);
                
                // Unobserve after revealing to only animate once
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    revealElements.forEach(el => {
        revealObserver.observe(el);
    });

    // 2. QUALIFICATION MODAL LOGIC
    const modal = document.getElementById('diagnostico-modal');
    const openBtns = document.querySelectorAll('.btn-open-modal');
    const closeBtn = document.querySelector('.modal-close');
    const steps = document.querySelectorAll('.modal-step');
    const nextBtns = document.querySelectorAll('.btn-next');
    const submitBtn = document.querySelector('.btn-submit');
    const empresaInput = document.getElementById('empresa-nome');
    
    // Open Modal
    openBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            modal.classList.add('active');
        });
    });

    // Close Modal
    const closeModal = () => modal.classList.remove('active');
    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });

    // Enable Next buttons when a radio is selected
    const radioGroups = document.querySelectorAll('.radio-group');
    radioGroups.forEach((group, index) => {
        const radios = group.querySelectorAll('input[type="radio"]');
        radios.forEach(radio => {
            radio.addEventListener('change', () => {
                if(nextBtns[index]) nextBtns[index].disabled = false;
            });
        });
    });

    // Next Step Logic
    nextBtns.forEach((btn, index) => {
        btn.addEventListener('click', () => {
            steps[index].classList.remove('active');
            if (steps[index + 1]) {
                steps[index + 1].classList.add('active');
            }
        });
    });

    // Enable Submit button when name is typed
    empresaInput.addEventListener('input', (e) => {
        submitBtn.disabled = e.target.value.trim() === '';
    });

    // Final Submit & WhatsApp Redirect
    submitBtn.addEventListener('click', () => {
        const operacao = document.querySelector('input[name="operacao"]:checked')?.value || "Não informado";
        const desafio = document.querySelector('input[name="desafio"]:checked')?.value || "Não informado";
        const empresa = empresaInput.value.trim() || "Empresa";

        const text = `Olá! Sou da *${empresa}*.\nNossa operação hoje funciona com:\n_-> ${operacao}_\n\nMas o que mais nos incomoda é:\n_-> ${desafio}_\n\nGostaria de agendar o diagnóstico técnico.`;
        
        const waUrl = `https://wa.me/559192432044?text=${encodeURIComponent(text)}`;
        window.open(waUrl, '_blank');
        closeModal();
    });

    // 3. SMART SCROLL NAVIGATION
    const nav = document.querySelector('.glass-nav');
    let lastScrollY = window.scrollY;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 150) {
            // Scroll down
            if (window.scrollY > lastScrollY) {
                nav.classList.add('nav-hidden');
            } 
            // Scroll up
            else {
                nav.classList.remove('nav-hidden');
            }
        } else {
            // Top of page
            nav.classList.remove('nav-hidden');
        }
        lastScrollY = window.scrollY;
    }, { passive: true });

    // 4. CINEMATIC SMOOTH SCROLL FOR MENU LINKS
    function smoothScroll(targetPosition, duration) {
        const startPosition = window.pageYOffset;
        const distance = targetPosition - startPosition;
        let startTime = null;

        // Easing function (easeInOutCubic)
        const ease = (t, b, c, d) => {
            t /= d / 2;
            if (t < 1) return c / 2 * t * t * t + b;
            t -= 2;
            return c / 2 * (t * t * t + 2) + b;
        };

        const animation = (currentTime) => {
            if (startTime === null) startTime = currentTime;
            const timeElapsed = currentTime - startTime;
            const run = ease(timeElapsed, startPosition, distance, duration);
            window.scrollTo(0, run);
            if (timeElapsed < duration) requestAnimationFrame(animation);
        };

        requestAnimationFrame(animation);
    }

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if(targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                // Calculate position with 80px offset for the sticky header padding
                const headerOffset = 80;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerOffset;
                
                // Scroll with 1200ms duration for a cinematic feel
                smoothScroll(targetPosition, 1200);
            }
        });
    });

});
