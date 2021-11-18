import { deleteIdea, getIdea } from "../api/data.js";
import { newEl } from "../dom.js";

const section = document.getElementById('detailsPage');
section.remove();

let context;
let ideaId;

const loadingEl = newEl('p', {}, 'Loading...');
const delButton = section.querySelector('.text-center');
delButton.remove();

export async function showDetailsPage(ctx, id) {
    ideaId = id;
    context = ctx;
    context.showSection(section);

    try {
        const idea = section.cloneNode(true);

        section.replaceChildren(loadingEl);

        const ideaData = await getIdea(id);

        idea.querySelector('img').src = ideaData.img;
        idea.querySelector('h2').textContent = ideaData.title;
        idea.querySelector('.idea-description').textContent = ideaData.description;

        const userData = JSON.parse(sessionStorage.getItem('userData'));

        if (userData !== null) {
            if (ideaData._ownerId === userData.id) {
                idea.appendChild(delButton);
            }
        }

        section.replaceChildren(...idea.childNodes);
    } catch (e) {
        context.goTo('home');
    }
}

section.addEventListener('click', async event => {
    event.preventDefault();
    if (event.target.tagName === 'A') {
        try {
            await deleteIdea(ideaId);
            context.goTo('catalog');
        } catch (err) {
            context.goTo('home');
        }
    }
});



