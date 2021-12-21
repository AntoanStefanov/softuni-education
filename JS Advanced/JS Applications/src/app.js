import { page, render } from './lib.js';
import { homePage } from './views/home.js';

/*
DEBUG purposes
*/
import * as api from './api/data.js';
window.api = api; // test login, register , functions
//

const root = document.querySelector('main');

page(decorateContext);
page('/', homePage);
// page('/memes', catalogPage);

page.start();

function decorateContext(ctx, next) {
  ctx.render = (template) => render(template, root);
  next();
}
