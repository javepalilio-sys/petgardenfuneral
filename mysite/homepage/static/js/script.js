document.addEventListener('DOMContentLoaded', function() {
    // Create floating petals on landing page
    createFloatingPetals();
});

function createFloatingPetals() {
    const container = document.querySelector('.petals-container');
    if (!container) return;

    function createPetal() {
        const petal = document.createElement('div');
        petal.className = 'petal';
        petal.style.left = Math.random() * 100 + '%';
        petal.style.top = '-10px';
        petal.style.delay = Math.random() * 2 + 's';
        container.appendChild(petal);

        setTimeout(() => {
            petal.remove();
        }, 8000);
    }

    setInterval(createPetal, 300);
}
