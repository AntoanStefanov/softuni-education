import * as api from '../api/data.js';


const section = document.getElementById("registerSection");
section.remove();

const form = section.querySelector("form");
form.addEventListener('submit', onSubmit);

let context;

export function showRegisterPage(ctx) {
    context = ctx;
    context.showSection(section);
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

    await api.register(email, password);

    context.updateUserNav();
    context.goTo('home');
}