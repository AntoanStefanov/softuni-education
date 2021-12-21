import { showSection, newEl, updateUserNav } from "./dom.js";
import { showLoginPage } from "./login.js";

const section = document.getElementById("catalogSection");
const ul = section.querySelector('ul');

section.remove();

export function showCatalogPage() {
    showSection(section);

    loadMovies();
}

async function loadMovies() {
    ul.replaceChildren(newEl('p', {}, 'Loading...'));

    const options = { method: 'GET', headers: {} };
    const userData = JSON.parse(sessionStorage.getItem('userData'));

    if (userData !== null) {
        options.headers['X-Authorization'] = userData.token;
    }

    const response = await fetch('http://localhost:3030/data/movies', options);
    
    if (response.status === 403) { 
        sessionStorage.removeItem('userData');
        updateUserNav();
        showLoginPage();
    }

    const movies = await response.json();

    ul.replaceChildren(...movies.map(createMovieCard));
}

function createMovieCard(movie) {
    return newEl('li', {}, movie.title);
}