const section = document.getElementById('homePage');
let context;

section.querySelector('#getStartedLink')
    .addEventListener('click', event => {
        event.preventDefault();
        context.goTo('catalog');
    });

section.remove();

export async function showHomePage(ctx) {
    context = ctx;
    context.showSection(section);
}
