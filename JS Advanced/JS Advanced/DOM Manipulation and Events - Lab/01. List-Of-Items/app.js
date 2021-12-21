function addItem() {
    let textToAdd = document.getElementById('newItemText').value;
    let newLiElement = document.createElement('li');
    newLiElement.appendChild(document.createTextNode(textToAdd));
    // newLiElement.textContent = textToAdd; 4 line replace
    let list = document.getElementById('items');
    list.appendChild(newLiElement);
}