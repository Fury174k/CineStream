// ==== Tab Switching Function ====
function openTab(event, tabId) {
    const tabContents = document.querySelectorAll('.tab-content');
    const tabButtons = document.querySelectorAll('.tab-btn');

    tabContents.forEach(content => {
        content.classList.add('hidden');
        content.classList.remove('active');
    });

    tabButtons.forEach(button => {
        button.classList.remove('active', 'border-red-600', 'text-white');
        button.classList.add('text-gray-400');
    });

    const selectedTab = document.getElementById(tabId);
    if (selectedTab) {
        selectedTab.classList.remove('hidden');
        selectedTab.classList.add('active');
    }

    event.currentTarget.classList.add('active', 'border-red-600', 'text-white');
    event.currentTarget.classList.remove('text-gray-400');
}

// ==== Review Modal Functions ====
function openReviewModal() {
    const modal = document.getElementById('review-modal');
    if (modal) modal.classList.remove('hidden');
}

function closeReviewModal() {
    const modal = document.getElementById('review-modal');
    if (modal) modal.classList.add('hidden');
}

// ==== Trailer Modal Functions ====
function playTrailer() {
    const modal = document.getElementById('trailer-modal');
    const iframe = document.getElementById('yt-player');
    const trailerId = document.getElementById('trailer-iframe')?.src?.split('/embed/')[1]?.split('?')[0];

    if (iframe && modal && trailerId) {
        iframe.src = `https://www.youtube.com/embed/${trailerId}?autoplay=1`;
        modal.classList.remove('hidden');
    }
}

function closeTrailerModal() {
    const modal = document.getElementById('trailer-modal');
    const iframe = document.getElementById('yt-player');

    if (iframe && modal) {
        iframe.src = "";
        modal.classList.add('hidden');
    }
}

// ==== Global Click Handler to Close Modals ====
window.onclick = function (event) {
    const reviewModal = document.getElementById('review-modal');
    const trailerModal = document.getElementById('trailer-modal');

    if (event.target === reviewModal) closeReviewModal();
    if (event.target === trailerModal) closeTrailerModal();
};

// ==== Circle Percentage Update (if applicable) ====
function updatePercentageCircle() {
    const circle = document.getElementById('percentage-circle');
    const text = document.getElementById('percentage-text');

    if (!circle || !text) return;

    let percentage = parseFloat(text.textContent);
    percentage = Math.ceil(percentage);
    circle.style.setProperty('--percentage', `${percentage}%`);
    text.textContent = `${percentage}%`;
}

// ==== DOM Ready Initializer ====
document.addEventListener('DOMContentLoaded', () => {
    updatePercentageCircle();
});
