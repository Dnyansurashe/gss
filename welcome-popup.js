// welcome-popup.js

// Show Welcome Popup Only Once
window.addEventListener('DOMContentLoaded', () => {
    // Check if "welcomeShown" is not set in localStorage
    if (!localStorage.getItem('welcomeShown')) {
        const popup = document.getElementById('welcomePopup');
        popup.classList.remove('hidden'); // Show the popup

        // Add event listener for "Enter" key to close popup
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                popup.classList.add('hidden'); // Hide the popup
                localStorage.setItem('welcomeShown', 'true'); // Set flag in localStorage
            }
        });
    }
});
