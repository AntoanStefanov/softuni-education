function validate() {
    let emailInput = document.getElementById('email');
    emailInput.addEventListener('change', function (event) {
        let email = event.target.value;
        const regex = /\b(?<name>[a-z]+)@(?<domain>[a-z]+)\.(?<extension>[a-z]+)\b/g;
        // return value of match method depends on g used or g NOT used


        // if (email.match(regex) !== null) {
        //     event.target.classList.remove('error');
        // } else {
        //     event.target.classList.add('error');
        // }
        // UP class attribute stays in the element class or class="error"
        // while down code - the attribute is GONE or class="error";
        // OR // 

        if (regex.test(email)) {
            event.target.removeAttribute('class');
        } else {
            event.target.setAttribute('class', 'error')
        }
    });
}