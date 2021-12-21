import page from '//unpkg.com/page/page.mjs';

const views = {
  '/home': () => '<h2>Home Page</h2>',
  '/catalog': () => '<h2>Catalog Page</h2>',
  '/catalog/kitchens': () => '<h2>Kitchen Page</h2>',
  '/about': () => '<h2>About Page</h2>',
};

const main = document.querySelector('main');

page('/home', () => showContent('/home'));
page('/catalog', () => showContent('/catalog'));
page('/catalog/kitchens', () => showContent('/catalog/kitchens'));
page('/about', () => showContent('/about'));
page.start();

showContent();

function showContent(name) {
  const view = views[name];

  if (typeof view === 'function') {
    main.innerHTML = view();
  } else {
    main.innerHTML = '<h2>ERRRRRRORRRRRRRRRRRRr</h2>';
  }
}
