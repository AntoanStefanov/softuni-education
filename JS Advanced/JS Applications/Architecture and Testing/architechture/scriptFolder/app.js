import { showAboutUsPage } from "./views/aboutUs.js";
import { showCatalogPage } from "./views/catalog.js";
import { showHomePage } from "./views/home.js";
import { showLoginPage } from "./views/login.js";
import { showRegisterPage } from "./views/register.js";
import { showSection } from "./dom.js";
import * as api from './api/data.js';


document.getElementById('logoutBtn').addEventListener('click', onLogout);
document.querySelector('nav').addEventListener('click', onNavigate);

const views = {
    'home': showHomePage,
    'catalog': showCatalogPage,
    'aboutUs': showAboutUsPage,
    'login': showLoginPage,
    'register': showRegisterPage
};

const links = {
    'homeBtn': 'home',
    'catalogBtn': 'catalog',
    'aboutUsBtn': 'aboutUs',
    'loginBtn': 'login',
    'registerBtn': 'register'
};


updateUserNav();

const context = {
    updateUserNav,
    goTo,
    showSection
};

goTo('home');

function onNavigate(event) {
    if (event.target.tagName === 'A') {
        const name = links[event.target.id];
        if (name) {
            event.preventDefault();
            goTo(name);
        }
    }
}

function goTo(name, ...params) {
    const view = views[name];
    if (typeof view === 'function') {
        view(context, ...params);
    }
}

async function onLogout(event) {
    event.stopImmediatePropagation();

    await api.logout();

    updateUserNav();
    goTo('home');

}

export function updateUserNav() {
    const userData = JSON.parse(sessionStorage.getItem('userData'));
    if (userData !== null) {
        document.getElementById('userNav').style.display = 'inline-block';
        document.getElementById('guestNav').style.display = 'none';
    } else {
        document.getElementById('userNav').style.display = 'none';
        document.getElementById('guestNav').style.display = 'inline-block';
    }
}




