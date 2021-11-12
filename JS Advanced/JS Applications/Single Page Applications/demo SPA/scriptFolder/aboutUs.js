import { showSection } from "./dom.js";

const section = document.getElementById("aboutUsSection");
section.remove();

export function showAboutUsPage() {
    showSection(section);
}