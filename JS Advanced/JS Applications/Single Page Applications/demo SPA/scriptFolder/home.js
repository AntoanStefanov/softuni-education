import { showSection, updateUserNav } from "./dom.js";

const section = document.getElementById("homeSection");
section.remove();

export function showHomePage() {
    showSection(section);
    updateUserNav();
}