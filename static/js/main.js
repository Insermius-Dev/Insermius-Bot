function plantStars() {
    for (let i = 0; i < 100; i++) {
        const star = document.createElement('div');
        star.classList.add('dot');

        star.style.left = `${Math.random() * 100}vw`;
        let height = document.body.scrollHeight;
        star.style.top = `${Math.random() * height}px`;
        star.style.width = `${Math.random() * 3}px`;
        star.style.animationDuration = `${Math.random() * 2 + 3}s`;
        star.style.animationDelay = `${Math.random() * 5 + 2}s`;
        document.body.appendChild(star);
    }

    // play the animation
    document.body.classList.add('fade-in-stars');
}

document.addEventListener("DOMContentLoaded", function() {
    plantStars();

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