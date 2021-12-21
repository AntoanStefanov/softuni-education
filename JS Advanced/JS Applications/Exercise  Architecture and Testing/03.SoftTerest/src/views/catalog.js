import { getAllIdeas } from "../api/data.js";
import { newEl } from '../dom.js';

const section = document.getElementById('dashboard-holder'); // structure
section.remove(); // structure

const templateDIV = section.querySelector('div');
const noIdeasTextEl = newEl('h1', {}, 'No ideas yet! Be the first one :)');
const loadingEl = newEl('p', {}, 'Loading...');

let context;

export async function showCatalogPage(ctx) {
  // structure
  context = ctx;
  context.showSection(section); // structure

  section.replaceChildren(loadingEl);
  try {
    const ideasData = await getAllIdeas(); // case - invalid token

    if (ideasData.length === 0) {
      section.replaceChildren(noIdeasTextEl);
      return;
    }

    let ideaElements = [];
    ideasData.forEach((ideaData) => {
      const idea = templateDIV.cloneNode(true);
      idea.querySelector('p').textContent = ideaData.title;
      idea.querySelector('img').src = ideaData.img;
      idea.querySelector('a').setAttribute('id', ideaData._id);

      ideaElements.push(idea);
    });

    section.replaceChildren(...ideaElements);
  } catch (err) {
    context.updateUserNav();
    context.goTo('catalog');
  }
}

section.addEventListener('click', (event) => {
  event.preventDefault();

  if (event.target.tagName === 'A') {
    context.goTo('details', event.target.id);
  }
});
