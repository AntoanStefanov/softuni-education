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

      let imageTD = document.createElement('td');
      let nameTD = document.createElement('td');
      let priceTD = document.createElement('td');
      let decFactorTD = document.createElement('td');
      let markTD = document.createElement('td');

      let imgEl = document.createElement('img');
      imgEl.setAttribute('src', object.img);
      imageTD.appendChild(imgEl);

      let nameP = document.createElement('p');
      nameP.textContent = object.name;
      nameTD.appendChild(nameP);

      let priceP = document.createElement('p');
      priceP.textContent = object.price;
      priceTD.appendChild(priceP);

      let decFactorP = document.createElement('p');
      decFactorP.textContent = object.decFactor;
      decFactorTD.appendChild(decFactorP);


      let inputEl = document.createElement('input');
      inputEl.setAttribute('type', 'checkbox');
      // inputEl.type = 'checkbox';
      markTD.appendChild(inputEl);


      newRow.appendChild(imageTD);
      newRow.appendChild(nameTD);
      newRow.appendChild(priceTD);
      newRow.appendChild(decFactorTD);
      newRow.appendChild(markTD);


      rows.appendChild(newRow);
    }
  })


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

    let productNames = products.join(', ');
    productNames = `Bought furniture: ${productNames}`;
    totalPrice = `Total price: ${totalPrice.toFixed(2)}`;
    totalDecFactor = `Average decoration factor: ${totalDecFactor / products.length}`;
    let outputList = [productNames, totalPrice, totalDecFactor];
    outputField.value = outputList.join('\n');
  })

}