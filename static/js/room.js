document.addEventListener('DOMContentLoaded', () => {
    // Function to update the percentage circle
    function updatePercentageCircle() {
        const circle = document.getElementById('percentage-circle');
        const text = document.getElementById('percentage-text');
        
        // Get the percentage from the HTML
        let percentage = parseFloat(text.textContent);
        
        percentage = Math.ceil(percentage);
        // Set the percentage for the circle
        circle.style.setProperty('--percentage', `${percentage}%`);
    
        // Update the text inside the circle
        text.textContent = `${percentage}%`;
    }

    // Call the function to update the circle based on the user score percentage from HTML
    updatePercentageCircle();
});

