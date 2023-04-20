
//This will apply the javascript responsiveness to the 
const form = document.getElementById('contact-form');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const subject = document.getElementById('subject').value;
  const message = document.getElementById('message').value;

  if (name === '' || email === '' || subject === '' || message === '') {
    alert('Please fill in all fields.');
    return;
  }

  const templateParams = {
    from_name: name,
    from_email: email,
    subject: subject,
    message_html: message
  };

  emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', templateParams)
    .then(() => {
      alert('Your message has been sent!');
      form.reset();
    }, (error) => {
      alert('Oops! Something went wrong. Please try again later.');
    });
});
