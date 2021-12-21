function editElement(reference, stringToReplace, replacer) {
    let text = reference.textContent;
    while (text.includes(stringToReplace)) {
        text = text.replace(stringToReplace, replacer);
    }
    reference.innerHTML = text;

//     reference.textContent = reference.textContent.replaceAll(stringToReplace, replacer);
// Tova ne minava v judje , no izglejda che bachka
};