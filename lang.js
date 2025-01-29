// script.js
document.querySelectorAll('.dropdown-content input[name="language"]').forEach(radio => {
    radio.addEventListener('change', function () {
        console.log(`Language selected: ${this.value}`);
        // You can add code here to dynamically change content based on the selected language
    });
});
