function solve() {
    let buttons = document.getElementsByTagName('button');
    let generateButton = buttons[0];
    let buyButton = buttons[1];
    let outputField = document.querySelector('#exercise textarea:disabled');
    let rows = document.querySelector('table.table tbody');

    generateButton.addEventListener('click', function (e) {
        let data = e.target.previousElementSibling.value;
        data = JSON.parse(data);
        for (let object of data) {
            let newRow = document.createElement('tr');

            let imageTD = createCell('img', { 'src': object.img }); // key as string  or
            let nameTD = createCell('p', {}, object.name);
            let priceTD = createCell('p', {}, object.price);
            let decFactorTD = createCell('p', {}, object.decFactor);
            let markTD = createCell('input', { type: 'checkbox' }); // key as what the fuck ?

            newRow.appendChild(imageTD);
            newRow.appendChild(nameTD);
            newRow.appendChild(priceTD);
            newRow.appendChild(decFactorTD);
            newRow.appendChild(markTD);

            rows.appendChild(newRow);
        }
    })

    function createCell(nestedTag, attributes, txtContent) {
        let cell = document.createElement('td');
        let nestedEl = document.createElement(nestedTag);

        for (let attr in attributes) {
            nestedEl.setAttribute(attr, attributes[attr])
        }
        if (txtContent !== undefined) { // or (txtContent)
            nestedEl.textContent = txtContent;
        }

        cell.appendChild(nestedEl);

        return cell;
    }

    buyButton.addEventListener('click', function (e) {
        let markedTDs = document.querySelectorAll('input[type="checkbox"]:checked');
        let products = [];
        let totalPrice = 0;
        let totalDecFactor = 0;

        for (let markedTD of markedTDs) {
            let rowCells = markedTD.parentElement.parentElement.cells;
            // textContent otdolu vzima na decata texta i konkatenira, no ima samo edin tekst taka che baca.
            // textContent returns the concatenation of the textContent of every child node,
            // excluding comments and processing instructions.
            // (This is an empty string if the node has no children.)
            // inache  rowCells[1].children[0].textContent , vzemane na teksta ot samiq paragraf
            products.push(rowCells[1].textContent);
            totalPrice += +rowCells[2].textContent;
            totalDecFactor += +rowCells[3].textContent;
        }
        let result = `Bought furniture: ${products.join(', ')}
Total price: ${totalPrice.toFixed(2)}
Average decoration factor: ${totalDecFactor / products.length}`

        outputField.value = result;
    })

}