const section = document.getElementById("aboutUsSection");
section.remove();

export function showAboutUsPage(ctx) {
    ctx.showSection(section);
}