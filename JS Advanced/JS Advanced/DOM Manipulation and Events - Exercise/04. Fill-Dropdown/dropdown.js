function addItem() {
    let menu = document.getElementById('menu');
    let textEl = document.getElementById('newItemText');
    let valueInputEl = document.getElementById('newItemValue');
    let optionElement = document.createElement('option');

    optionElement.textContent = textEl.value;

    optionElement.setAttribute('value', valueInputEl.value);
    // optionElement.value = valueInputEl.value;

    menu.appendChild(optionElement);
    
    textEl.value = '';
    valueInputEl.value = ''; 
}