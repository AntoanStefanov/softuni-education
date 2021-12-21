import { showSection } from "./dom.js";
import { showHomePage } from "./home.js";

const section = document.getElementById("loginSection");
section.remove();

const form = section.querySelector("form");
form.addEventListener('submit', onSubmit);

export function showLoginPage() {
    showSection(section);
}

async function onSubmit(event) {
    event.preventDefault();

    const formData = new FormData(form);

    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    form.reset();

    if (email === '' || password === '') {
        alert('Fill empty input/s');
        return;
    }

    try {
        const res = await fetch('http://localhost:3030/users/login', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        if (res.ok !== true) {
            const error = await res.json();
            throw new Error(error.message);
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