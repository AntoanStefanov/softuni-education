window.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form#register');
    form.addEventListener('submit', onRegister);
    document.getElementById('logout').style.display = 'none';
});

function onRegister(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    const rePass = formData.get('rePass').trim();

    registerUser(email, password, rePass)
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


async function registerUser(email, password, rePass) {

    if (password !== rePass) {
        throw new Error("Passwords don't match");
    }

    const URL = 'http://localhost:3030/users/register';

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