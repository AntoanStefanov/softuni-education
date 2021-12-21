import { createIdea } from "../api/data.js";

const section = document.getElementById('createPage');
section.remove();

const form = section.querySelector("form");
form.addEventListener('submit', onSubmit);

let context;

export async function showCreatePage(ctx) {
    context = ctx;
    context.showSection(section);
}

async function onSubmit(event) {
    event.preventDefault();
    const formData = new FormData(form);

    const title = formData.get('title').trim();
    const description = formData.get('description').trim();
    const img = formData.get('imageURL').trim();

    form.reset();

    if (areInputsValid(title, description, img)) {
        try {
            await createIdea({ title, description, img });
            context.goTo('catalog');
        } catch (err) {
            context.updateUserNav();
            context.goTo('login');
        }
    }
}

function areInputsValid(title, description, img) {
    if (title === '' || description === '' || img === '') {
        alert('Fill empty input/s');
        return;
    }

    if (title.length < 6) {
        alert('Invalid Title! At least six chars');
        return;
    }

    if (description.length < 10) {
        alert('Invalid Description! At least ten chars');
        return;
    }

    if (img.length < 5) {
        alert('Invalid Image URL! At least five chars');
        return;
    }

    return true;
}


