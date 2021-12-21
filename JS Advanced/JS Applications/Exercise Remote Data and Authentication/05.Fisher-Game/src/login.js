// script run after page loaded - DOMContentLoaded
window.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form#login');
    form.addEventListener('submit', onLogin);
    document.getElementById('logout').style.display = 'none';
});

function onLogin(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    const email = formData.get('email').trim();
    const password = formData.get('password').trim();

    loginUser(email, password)
        .then(userInfo => {
            const userData = {
                email: userInfo.email,
                id: userInfo._id,
                token: userInfo.accessToken
            };

            sessionStorage.setItem('userData', JSON.stringify(userData));

            window.location = './index.html';
        })
        .catch(error => {
            alert('Error: ' + error.message);
        });

    event.target.reset();
}

async function loginUser(email, password) {
    const URL = 'http://localhost:3030/users/login';

    const body = {
        email,
        password
    };

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    }

    const response = await fetch(URL, options);

    if (response.ok != true) {
        const error = await response.json();
        throw new Error(error.message);
    }

    const userInfo = await response.json();

    return userInfo;
}