document.addEventListener('DOMContentLoaded', () => {
    const navButton = document.getElementById('nav-button');
    const menuSection = document.getElementById('menu-section'); 
    const closeMenu = document.getElementById('close-menu');
    let menuIsActive = false;

    navButton.addEventListener('click', () => {
        if (!menuIsActive) {
            menuSection.style.top = '0';
            menuSection.style.display = 'flex';
            menuIsActive = true;
        }
    });

    closeMenu.addEventListener('click', () => {
        menuSection.style.top = '-250%';
        menuSection.style.display = 'none';
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

    // Hide loading animation if the page is loaded from the cache
    window.addEventListener('pageshow', (event) => {
        if (event.persisted) {
            hideLoading();
        }
    });

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

function showAlert(type, message) {
    const alertContainer = document.getElementById('alert-container');
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.innerHTML = `
        <span>${message}</span>
        <button class="close-alert">&times;</button>
    `;
    alertContainer.appendChild(alert);

    // Slide in the alert
    setTimeout(() => {
        alert.classList.add('show');
    }, 100);

    // Auto-hide after 5 seconds
    setTimeout(() => {
        alert.classList.remove('show');
        setTimeout(() => {
            alert.remove();
        }, 300);
    }, 5000);

    // Close alert on button click
    alert.querySelector('.close-alert').addEventListener('click', () => {
        alert.classList.remove('show');
        setTimeout(() => {
            alert.remove();
        }, 300);
    });
}