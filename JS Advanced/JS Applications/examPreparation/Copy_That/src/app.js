import { page, render } from './lib.js';
// import { homePage } from './views/home.js';
import { catalogPage } from './views/catalog.js';
import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';
import { logout } from './api/data.js';
import { getUserData } from './util.js';
import { createPage } from './views/create.js';
import { detailsPage } from './views/details.js';
import { editPage } from './views/edit.js';
import { profilePage } from './views/profile.js';

/*
DEBUG purposes
*/
import * as api from './api/data.js';
window.api = api; // test login, register , functions
//

const root = document.querySelector('main');
document.getElementById('logoutBtn').addEventListener('click', onLogout);

page(decorateContext);
// page('/', homePage);
page('/catalog', catalogPage);
page('/login', loginPage);
page('/register', registerPage);
page('/create', createPage);
page('/details/:id', detailsPage); // tuka id e placeholder, moje vsqko id da vleze i v ctx otiva kato parameter
page('/edit/:id', editPage); // tuka id e placeholder, moje vsqko id da vleze i v ctx otiva kato parameter
page('/profile', profilePage);

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
  page.redirect('/catalog');
}

// tuk se smenq SELECTORA SPRQMO HTML KOITO E DADEN ZA NAVIGACIQTA
function updateUserNav() {
  const userData = getUserData();
  if (userData) {
    document.querySelector('#user').style.display = 'block';
    document.querySelector('#guest').style.display = 'none';
    document.querySelector(
      '#user span'
    ).textContent = `Welcome, ${userData.email}`;
  } else {
    document.querySelector('#user').style.display = 'none';
    document.querySelector('#guest').style.display = 'block';
  }
}
