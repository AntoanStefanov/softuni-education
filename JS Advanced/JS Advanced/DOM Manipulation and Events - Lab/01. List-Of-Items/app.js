function addItem() {
    let textToAdd = document.getElementById('newItemText').value;
    let newLiElement = document.createElement('li');
    newLiElement.appendChild(document.createTextNode(textToAdd));
    let list = document.getElementById('items');
    list.appendChild(newLiElement);
}