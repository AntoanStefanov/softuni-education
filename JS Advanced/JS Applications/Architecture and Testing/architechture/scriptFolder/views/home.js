const section = document.getElementById("homeSection");
section.remove();

export function showHomePage(ctx) {
    ctx.showSection(section);
}