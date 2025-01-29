let searchForm = document.querySelector('.search-form');

document.querySelector('#search-btn').onclick = () =>{
    searchForm.classList.toggle('active');
    shoppingCart.classList.remove('active');
    loginForm.classList.remove('active');
    navbar.classList.remove('active');
}

let shoppingCart = document.querySelector('.shopping-cart');

document.querySelector('#cart-btn').onclick = () =>{
    shoppingCart.classList.toggle('active');
    searchForm.classList.remove('active');
    loginForm.classList.remove('active');
    navbar.classList.remove('active');
}

let loginForm = document.querySelector('.login-form');

document.querySelector('#login-btn').onclick = () =>{
    loginForm.classList.toggle('active');
    searchForm.classList.remove('active');
    shoppingCart.classList.remove('active');
    navbar.classList.remove('active');
}

let navbar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');
    searchForm.classList.remove('active');
    shoppingCart.classList.remove('active');
    loginForm.classList.remove('active');
}

window.onscroll = () =>{
    searchForm.classList.remove('active');
    shoppingCart.classList.remove('active');
    loginForm.classList.remove('active');
    navbar.classList.remove('active');
}

var swiper = new Swiper(".product-slider", {
    loop:true,
    spaceBetween: 20,
    autoplay: {
        delay: 7500,
        disableOnInteraction: false,
    },
    centeredSlides: true,
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1020: {
        slidesPerView: 3,
      },
    },
});

var swiper = new Swiper(".review-slider", {
    loop:true,
    spaceBetween: 20,
    autoplay: {
        delay: 7500,
        disableOnInteraction: false,
    },
    centeredSlides: true,
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1020: {
        slidesPerView: 3,
      },
    },
});
document.getElementById('menu-btn').addEventListener('click', function() {
  this.classList.toggle('open');
  document.querySelector('.navbar').classList.toggle('open');
});

// Live Search Suggestions (Example Function)
function showSuggestions(query) {
  const suggestions = document.getElementById('suggestions');
  if (query.length > 0) {
      suggestions.style.display = 'block';
      // Sample data for demo (replace with dynamic suggestions as needed)
      const sampleSuggestions = [
          'Apple', 'Banana', 'Orange', 'Broccoli', 'Carrots', 'Spinach'
      ].filter(item => item.toLowerCase().includes(query.toLowerCase()));
      
      suggestions.innerHTML = sampleSuggestions.map(item => `<a href="/search?q=${item}">${item}</a>`).join('');
  } else {
      suggestions.style.display = 'none';
  }
}

// Hide suggestions when clicking outside
document.addEventListener('click', (e) => {
  if (!e.target.closest('.search-form')) {
      document.getElementById('suggestions').style.display = 'none';
  }
});