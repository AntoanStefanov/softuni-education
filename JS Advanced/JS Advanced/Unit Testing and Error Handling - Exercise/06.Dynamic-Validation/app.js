function validate() {
    let emailInput = document.getElementById('email');
    emailInput.addEventListener('change', function (event) {
        let email = event.target.value;
        const regex = /\b(?<name>[a-z]+)@(?<domain>[a-z]+)\.(?<extension>[a-z]+)\b/g; 
        // return value of match method depends on g used or g NOT used, check mdn ? match ?
        if (email.match(regex) !== null) {
            event.target.classList.remove('error');
        } else {
            event.target.classList.add('error');
        }
    });
}