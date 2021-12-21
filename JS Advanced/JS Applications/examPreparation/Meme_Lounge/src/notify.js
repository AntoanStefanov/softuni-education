const errorBoxNotify = document.getElementById('errorBox');
const message = errorBoxNotify.querySelector('span');

export function notify(msg) {
  message.textContent = msg;
  errorBoxNotify.style.display = 'block';

  setTimeout(() => (errorBoxNotify.style.display = 'none'), 3000);
}
