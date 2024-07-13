document.addEventListener("DOMContentLoaded", function() {
    const star = document.querySelector('.star');

    // Remove initial animation class after it completes
    star.addEventListener('animationend', (e) => {
        if (e.animationName === 'fadeInStar') {
            star.classList.remove('load-animation');
        }
    });

    // Add click event listener
    star.addEventListener('click', function() {
        // Remove any previous click-animation to restart the animation
        star.classList.remove('click-animation');
        // Trigger reflow for restart animation
        void star.offsetWidth;
        // Add click-animation class
        star.classList.add('click-animation');
    });
});