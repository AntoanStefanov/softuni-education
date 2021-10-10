function notify(message) {
  let notificationDivEl = document.getElementById('notification');
  notificationDivEl.style.display = 'block';
  notificationDivEl.textContent = message;


  notificationDivEl.addEventListener('click', function (event) {
    notificationDivEl.style.display = 'none';
  });

}