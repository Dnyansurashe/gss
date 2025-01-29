// Select the login form
const loginForm = document.getElementById('loginForm');

// Handle form submission
loginForm.onsubmit = function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get input values
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Simple validation (You can add more complex logic here)
    if (email && password) {
        // Simulate login success by redirecting to another page
        window.location.href = 'dashboard.html'; // Redirect to another page
    } else {
        alert('Please enter both email and password!');
    }
};
