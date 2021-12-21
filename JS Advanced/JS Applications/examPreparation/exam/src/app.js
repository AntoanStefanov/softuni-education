import { page, render } from './lib.js';
import { homePage } from './views/home.js';
import { catalogPage } from './views/catalog.js';
import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';
import { logout } from './api/data.js';
import { getUserData } from './util.js';
import { createPage } from './views/create.js';
import { detailsPage } from './views/details.js';
import { editPage } from './views/edit.js';

/*
DEBUG purposes
*/
import * as api from './api/data.js';
import { searchPage } from './views/search.js';
window.api = api; // test login, register , functions
//

const root = document.querySelector('main');
document.getElementById('logoutBtn').addEventListener('click', onLogout);

page(decorateContext);
page('/', homePage);
page('/catalog', catalogPage);
page('/login', loginPage);
page('/register', registerPage);
page('/create', createPage);
page('/details/:id', detailsPage); // tuka id e placeholder, moje vsqko id da vleze i v ctx otiva kato parameter
page('/edit/:id', editPage); // tuka id e placeholder, moje vsqko id da vleze i v ctx otiva kato parameter
page('/search', searchPage);

updateUserNav(); // start na prilojenieto, podgotovka
page.start();

function decorateContext(ctx, next) {
  ctx.render = (template) => render(template, root);
  ctx.updateUserNav = updateUserNav;
  next();
}

async function onLogout() {
  logout();
  updateUserNav();
  page.redirect('/');
}

// tuk se smenq SELECTORA SPRQMO HTML KOITO E DADEN ZA NAVIGACIQTA
function updateUserNav() {
  const userData = getUserData();
  if (userData) {
    [...document.querySelectorAll('.userNav')].forEach(
      (li) => (li.style.display = 'inline-block')
    );
    [...document.querySelectorAll('.guestNav')].forEach(
      (li) => (li.style.display = 'none')
    );
  } else {
    [...document.querySelectorAll('.userNav')].forEach(
      (li) => (li.style.display = 'none')
    );
    [...document.querySelectorAll('.guestNav')].forEach(
      (li) => (li.style.display = 'inline-block')
    );
  }
}
