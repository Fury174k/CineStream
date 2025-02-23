document.addEventListener('DOMContentLoaded', () => {
    // Celebrity section scroll handling
    const celebrityContainer = document.getElementById('celebrities-container');
    const nextButton = document.getElementById('celebrity-list__next');
    const prevButton = document.getElementById('celebrity-list__prev');
    const scrollAmount = 600; // Increased amount to scroll

    if (celebrityContainer && nextButton && prevButton) {
        nextButton.addEventListener('click', () => {
            celebrityContainer.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });

        prevButton.addEventListener('click', () => {
            celebrityContainer.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });

        function checkCelebrityScroll() {
            if (celebrityContainer.scrollLeft + celebrityContainer.clientWidth >= celebrityContainer.scrollWidth * 0.9) {
                nextButton.style.display = 'none';
            } else {
                nextButton.style.display = 'block';
            }

            if (celebrityContainer.scrollLeft === 0) {
                prevButton.style.display = 'none';
            } else {
                prevButton.style.display = 'block';
            }
        }

        celebrityContainer.addEventListener('scroll', checkCelebrityScroll);
        checkCelebrityScroll();
    }

    // Initialize Vanilla Tilt on elements with the data-tilt attribute
    VanillaTilt.init(document.querySelectorAll("[data-tilt]"), {
        max: 25,
        speed: 400
    });

    // Top movies section scroll handling
    const topMoviesContainer = document.getElementById('top-movies-container');
    const topNextButton = document.getElementById('top-movie-list__next');
    const topPrevButton = document.getElementById('top-movie-list__prev');

    if (topMoviesContainer && topNextButton && topPrevButton) {
        topNextButton.addEventListener('click', () => {
            topMoviesContainer.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });

        topPrevButton.addEventListener('click', () => {
            topMoviesContainer.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });

        function checkTopMoviesScroll() {
            if (topMoviesContainer.scrollLeft + topMoviesContainer.clientWidth >= topMoviesContainer.scrollWidth * 0.9) {
                topNextButton.style.display = 'none';
            } else {
                topNextButton.style.display = 'block';
            }

            if (topMoviesContainer.scrollLeft === 0) {
                topPrevButton.style.display = 'none';
            } else {
                topPrevButton.style.display = 'block';
            }
        }

        topMoviesContainer.addEventListener('scroll', checkTopMoviesScroll);
        checkTopMoviesScroll();
    }

    // Popular genres section scroll handling
    const popularGenresContainer = document.getElementById('popular-genre-container');
    const popularNextButton = document.getElementById('popular-genre-list__next');
    const popularPrevButton = document.getElementById('popular-genre-list__prev');

    if (popularGenresContainer && popularNextButton && popularPrevButton) {
        popularNextButton.addEventListener('click', () => {
            popularGenresContainer.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });

        popularPrevButton.addEventListener('click', () => {
            popularGenresContainer.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });

        function checkPopularGenresScroll() {
            if (popularGenresContainer.scrollLeft + popularGenresContainer.clientWidth >= popularGenresContainer.scrollWidth * 0.9) {
                popularNextButton.style.display = 'none';
            } else {
                popularNextButton.style.display = 'block';
            }

            if (popularGenresContainer.scrollLeft === 0) {
                popularPrevButton.style.display = 'none';
            } else {
                popularPrevButton.style.display = 'block';
            }
        }

        popularGenresContainer.addEventListener('scroll', checkPopularGenresScroll);
        checkPopularGenresScroll();
    }

    // Upcoming movies section scroll handling
    const comingSoonContainer = document.getElementById('comingsoon-list-container');
    const comingSoonNextButton = document.getElementById('comingsoon-list__next');
    const comingSoonPrevButton = document.getElementById('comingsoon-list__prev');

    if (comingSoonContainer && comingSoonNextButton && comingSoonPrevButton) {
        comingSoonNextButton.addEventListener('click', () => {
            comingSoonContainer.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });

        comingSoonPrevButton.addEventListener('click', () => {
            comingSoonContainer.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });

        function checkComingSoonScroll() {
            if (comingSoonContainer.scrollLeft + comingSoonContainer.clientWidth >= comingSoonContainer.scrollWidth * 0.9) {
                comingSoonNextButton.style.display = 'none';
            } else {
                comingSoonNextButton.style.display = 'block';
            }

            if (comingSoonContainer.scrollLeft === 0) {
                comingSoonPrevButton.style.display = 'none';
            } else {
                comingSoonPrevButton.style.display = 'block';
            }
        }

        comingSoonContainer.addEventListener('scroll', checkComingSoonScroll);
        checkComingSoonScroll();
    }

    // Celebrities born today section scroll handling
    const bornTodayContainer = document.getElementById('born-today-list-container');
    const bornTodayNextButton = document.getElementById('born-today-list__next');
    const bornTodayPrevButton = document.getElementById('born-today-list__prev');

    if (bornTodayContainer && bornTodayNextButton && bornTodayPrevButton) {
        bornTodayNextButton.addEventListener('click', () => {
            bornTodayContainer.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });

        bornTodayPrevButton.addEventListener('click', () => {
            bornTodayContainer.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });

        function checkBornTodayScroll() {
            if (bornTodayContainer.scrollLeft + bornTodayContainer.clientWidth >= bornTodayContainer.scrollWidth * 0.9) {
                bornTodayNextButton.style.display = 'none';
            } else {
                bornTodayNextButton.style.display = 'block';
            }

            if (bornTodayContainer.scrollLeft === 0) {
                bornTodayPrevButton.style.display = 'none';
            } else {
                bornTodayPrevButton.style.display = 'block';
            }
        }

        bornTodayContainer.addEventListener('scroll', checkBornTodayScroll);
        checkBornTodayScroll();
    }
});