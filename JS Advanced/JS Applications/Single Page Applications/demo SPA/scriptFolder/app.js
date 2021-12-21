import { showAboutUsPage } from "./aboutUs.js";
import { showCatalogPage } from "./catalog.js";
import { showHomePage } from "./home.js";
import { showLoginPage } from "./login.js";
import { onLogout } from "./logout.js";
import { showRegisterPage } from "./register.js";

document.querySelector('nav').addEventListener('click', navOnClick);

const sections = {
    'homeBtn': showHomePage,
    'catalogBtn': showCatalogPage,
    'aboutUsBtn': showAboutUsPage,
    'loginBtn': showLoginPage,
    'registerBtn': showRegisterPage,
    'logoutBtn': onLogout
}

showHomePage();

function navOnClick(event) {
    if (event.target.tagName === 'A') {

        const view = sections[event.target.id];

        if (typeof view === 'function') {
            // chak tuk prevent, za da moje ako e link kum google da go otvori
            // <!-- <a href="https://www.google.com/?hl=bg">Google</a> -->
            event.preventDefault();
            view();
        }
    }
}



