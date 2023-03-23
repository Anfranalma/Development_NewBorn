// Variables to store the DOM elements we will be manipulating
const nav = document.querySelector('nav');
const menuBtn = document.querySelector('.menu-btn');
const gallery = document.querySelector('.gallery');
const form = document.querySelector('form');
const message = document.querySelector('.message');
const closeBtn = document.querySelector('.close-btn');

// Toggle the mobile navigation menu
menuBtn.addEventListener('click', () => {
  nav.classList.toggle('show');
});

// Close the mobile navigation menu when a link is clicked
nav.addEventListener('click', () => {
  nav.classList.remove('show');
});

// Display a larger version of the image when it is clicked
gallery.addEventListener('click', (e) => {
  if (e.target.tagName === 'IMG') {
    const imgSrc = e.target.getAttribute('src');
    const modal = document.createElement('div');
    modal.classList.add('modal');
    modal.innerHTML = `
      <div class="modal-content">
        <img src="${imgSrc}">
      </div>
    `;
    document.body.appendChild(modal);
    modal.addEventListener('click', () => {
      modal.remove();
    });
  }
});

// Submit the contact form via AJAX
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  const response = await fetch('/send', {
    method: 'POST',
    body: formData,
  });
  const result = await response.json();
  if (result.success) {
    form.reset();
    message.innerHTML = 'Thanks for your message! We will get back to you shortly.';
    message.classList.add('success');
  } else {
    message.innerHTML = 'There was an error sending your message. Please try again.';
    message.classList.add('error');
  }
});

// Close the message box
closeBtn.addEventListener('click', () => {
  message.classList.remove('success', 'error');
  message.innerHTML = '';
});
