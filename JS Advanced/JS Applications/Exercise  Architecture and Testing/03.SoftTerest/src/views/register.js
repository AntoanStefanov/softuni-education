import * as api from '../api/data.js';


const section = document.getElementById('registerPage');
section.remove();
section.querySelector('p').remove();

const form = section.querySelector("form");
form.addEventListener('submit', onSubmit);

let context;

export async function showRegisterPage(ctx) {
    context = ctx;
    context.showSection(section);
}

async function onSubmit(event) {
    event.preventDefault();
    const formData = new FormData(form);

    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    const rePass = formData.get('repeatPassword').trim();

    form.reset();

    if (areInputsValid(email, password, rePass)) {
        await api.register(email, password);
        context.updateUserNav();
        context.goTo('home');
    }
}

function areInputsValid(email, password, rePass) {
    const specialCharRegex = new RegExp('.*[!@#$%^&_*]');
    const numRegex = new RegExp('.*[0-9]');

    if (email === '' || password === '' || rePass === '') {
        alert('Fill empty input/s');
        return;
    }

    if (email.length < 3) {
        alert('Invalid Email! At least three chars');
        return;
    }

    // if (!numRegex.test(email)) {
    //     alert('Invalid Email! At least one digit');
    //     return;
    // }

    if (!specialCharRegex.test(email)) {
        alert('Invalid Email! At least one special char');
        return;
    }

    if (password.length < 3) {
        alert('Invalid Password! At least three chars');
        return;
    }

    if (password !== rePass) {
        alert('Passwords don\'t match.');
        return;
    }

    return true;
}