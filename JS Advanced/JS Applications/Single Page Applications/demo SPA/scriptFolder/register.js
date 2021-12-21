import { showSection } from "./dom.js";
import { showHomePage } from "./home.js";

const section = document.getElementById("registerSection");
section.remove();

const form = section.querySelector("form");
form.addEventListener('submit', onSubmit);

export function showRegisterPage() {
    showSection(section);
}

async function onSubmit(event) {
    event.preventDefault();
    const formData = new FormData(form);

    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    const rePass = formData.get('rePass').trim();

    form.reset();

    if (email === '' || password === '' || rePass === '') {
        alert('Fill empty input/s');
        return;
    }

    if (password !== rePass) {
        alert('Passwords don\'t match.');
        return;
    }

    try {
        const res = await fetch('http://localhost:3030/users/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        if (res.ok !== true) {
            const err = await response.json();
            throw new Error(err.message);
        }

        const data = await res.json();
        
        const userData = {
            email: data.email,
            id: data._id,
            token: data.accessToken
        };

        sessionStorage.setItem('userData', JSON.stringify(userData));
        showHomePage();

    } catch (err) {
        alert(err.message);
    }
}