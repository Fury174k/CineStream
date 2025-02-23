console.log("Hello world!");

document.addEventListener('DOMContentLoaded', () => {
    navButton = document.getElementById('nav-button');
    menuSection = document.getElementById('menu-section'); 
    closeMenu = document.getElementById('close-menu');
    let menuIsActive = false;

    navButton.addEventListener('click', () => {
        if (!menuIsActive) {
            menuSection.style.top = '0';
            menuSection.display = 'flex';
            menuIsActive = true;
        }
    });

    closeMenu.addEventListener('click', () => {
        menuSection.style.top = '-250%';
        menuSection.display = 'none';
        menuIsActive = false;
    });

    const loadingOverlay = document.querySelector('.loading-overlay');

    function showLoading() {
        loadingOverlay.style.display = 'flex';
    }

    function hideLoading() {
        loadingOverlay.style.display = 'none';
    }

    // Show loading animation on page load
    showLoading();

    // Hide loading animation after the page has fully loaded
    window.addEventListener('load', hideLoading);

    // Show loading animation when a link is clicked
    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', (event) => {
            // Prevent showing the loading overlay for anchor links
            if (link.getAttribute('href').startsWith('#')) return;
            showLoading();
        });
    });

    // Show loading animation when a form is submitted
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', () => {
            showLoading();
        });
    });

    // Optionally, show loading animation on AJAX requests
    document.addEventListener('ajaxStart', showLoading);
    document.addEventListener('ajaxStop', hideLoading);
    document.addEventListener('ajaxError', hideLoading);
});