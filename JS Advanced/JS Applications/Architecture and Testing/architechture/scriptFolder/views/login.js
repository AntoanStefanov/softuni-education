import * as api from '../api/data.js';

const section = document.getElementById("loginSection");
section.remove();

const form = section.querySelector("form");
form.addEventListener('submit', onSubmit);

let context;

export function showLoginPage(ctx) {
    context = ctx;
    context.showSection(section);
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

    await api.login(email, password);
    context.updateUserNav();
    context.goTo('home');
}

