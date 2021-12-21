import { showHomePage } from './views/home.js';
import { showCatalogPage } from './views/catalog.js';
import { showLoginPage } from './views/login.js';
import { showRegisterPage } from './views/register.js';
import { showCreatePage } from './views/create.js';
import { showDetailsPage } from './views/details.js';
import { showSection } from './dom.js';
import { logout } from './api/data.js';

const links = {
    'homeLink': 'home',
    'getStartedLink': 'home',
    'catalogLink': 'catalog',
    'loginLink': 'login',
    'registerLink': 'register',
    'createLink': 'create'

};

const views = {
    'home': showHomePage,
    'catalog': showCatalogPage,
    'login': showLoginPage,
    'register': showRegisterPage,
    'create': showCreatePage,
    'details': showDetailsPage
};

const nav = document.querySelector('nav');

document.getElementById('logoutBtn').addEventListener('click', onLogout);
nav.addEventListener('click', onNavigate);

const ctx = {
    goTo,
    showSection,
    updateUserNav
};

// start app in home view
updateUserNav();
goTo('home');

function onNavigate(event) {
    const name = links[event.target.id];
    if (name) {
        event.preventDefault();
        goTo(name);
    }
}

function goTo(name, ...params) {
    const view = views[name];
    if (typeof view === 'function') {
        view(ctx, ...params);
    }
}

async function onLogout(event) {
    event.stopImmediatePropagation();
    event.preventDefault(); // zaradi a href = "" ?, neshto stava i failva fetcha

    await logout();

    updateUserNav();
    goTo('home');
}

export function updateUserNav() {
    const userData = JSON.parse(sessionStorage.getItem('userData'));
    if (userData !== null) {
        document.querySelectorAll('.userNav')
            .forEach(btn => btn.style.display = 'inline-block');
        document.querySelectorAll('.guestNav')
            .forEach(btn => btn.style.display = 'none');
    } else {
        document.querySelectorAll('.userNav')
            .forEach(btn => btn.style.display = 'none');
        document.querySelectorAll('.guestNav')
            .forEach(btn => btn.style.display = 'inline-block');
    }
}