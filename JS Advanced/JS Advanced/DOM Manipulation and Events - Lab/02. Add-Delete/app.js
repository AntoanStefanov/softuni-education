function addItem() {
    // creating link // 
    let a = document.createElement('a');
    let linkText = document.createTextNode('[Delete]');
    a.appendChild(linkText);
    a.setAttribute('href', '#');
    //

    // from 1st task code.
    let textToAdd = document.getElementById('newItemText').value;
    let newLiElement = document.createElement('li');
    newLiElement.appendChild(document.createTextNode(textToAdd));
    // newLiElement.textContent = textToAdd; 12 line replacer.
    newLiElement.appendChild(a);
    //

    // a.addEventListener('click', function(e) {
    //     newLiElement.remove();
    // })

    let list = document.getElementById('items');
    list.appendChild(newLiElement);

    list.addEventListener('click', function(event) {
        if (event.target.tagName === 'A') {
            let item = event.target.parentElement;
            item.remove();
        }
        
    });

}