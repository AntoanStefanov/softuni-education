window.addEventListener('load', solve);
// 17:50 - 18:56; 1h 6 mins;
function solve() {
    let modelEl = document.getElementById('model');
    let yearEl = document.getElementById('year');
    let descriptionEl = document.getElementById('description');
    let priceEl = document.getElementById('price');
    let tableBodyEl = document.getElementById('furniture-list');
    let addButton = document.getElementById('add');
    let totalPriceEl = document.getElementsByClassName('total-price')[0];

    addButton.addEventListener('click', function (e) {
        e.preventDefault();
        if (modelEl.value !== '' && descriptionEl.value !== '') {
            if (priceEl.value !== '' && yearEl.value !== '') {
                let price = Number(priceEl.value);
                let year = Number(yearEl.value);
                if (price >= 0 && year >= 0) {  
                    let firstTR = document.createElement('tr');
                    firstTR.setAttribute('class', 'info');
                    let firstTDforFirstTR = document.createElement('td');
                    let secondTDforFirstTR = document.createElement('td');
                    firstTDforFirstTR.textContent = modelEl.value;
                    secondTDforFirstTR.textContent = price.toFixed(2);

                    let thirdTDforFirstTR = document.createElement('td');

                    let firstButtonForThirdTD = document.createElement('button');
                    firstButtonForThirdTD.setAttribute('class', 'moreBtn');
                    firstButtonForThirdTD.textContent = 'More Info';

                    let secondButtonForThirdTD = document.createElement('button');
                    secondButtonForThirdTD.setAttribute('class', 'buyBtn');
                    secondButtonForThirdTD.textContent = 'Buy it';

                    thirdTDforFirstTR.appendChild(firstButtonForThirdTD);
                    thirdTDforFirstTR.appendChild(secondButtonForThirdTD);

                    firstTR.appendChild(firstTDforFirstTR);
                    firstTR.appendChild(secondTDforFirstTR);
                    firstTR.appendChild(thirdTDforFirstTR);



                    let secondTR = document.createElement('tr');
                    secondTR.setAttribute('class', 'hide');
                    let firstTDforSecondTR = document.createElement('td');
                    let secondTDforSecondTR = document.createElement('td');
                    secondTDforSecondTR.setAttribute('colspan', '3');
                    firstTDforSecondTR.textContent = `Year: ${year}`;
                    secondTDforSecondTR.textContent = `Description: ${descriptionEl.value}`;

                    secondTR.appendChild(firstTDforSecondTR);
                    secondTR.appendChild(secondTDforSecondTR);

                    tableBodyEl.appendChild(firstTR);
                    tableBodyEl.appendChild(secondTR);

                    firstButtonForThirdTD.addEventListener('click', function () {
                        if (firstButtonForThirdTD.textContent == 'More Info') {
                            firstButtonForThirdTD.textContent = 'Less Info';
                            secondTR.setAttribute('style', 'display: contents;');
                        } else {
                            firstButtonForThirdTD.textContent = 'More Info';
                            secondTR.setAttribute('style', 'display: none;');
                        }
                    });

                    secondButtonForThirdTD.addEventListener('click', function (e) {
                        let price = e.target.parentElement.parentElement.querySelector('td:nth-child(2)').textContent;
                        e.target.parentElement.parentElement.nextElementSibling.remove();
                        e.target.parentElement.parentElement.remove();
                        let sum = Number(price) + Number(totalPriceEl.textContent);
                        totalPriceEl.textContent = sum.toFixed(2);

                    }); 
                    
                    modelEl.value = ''; 
                    yearEl.value = ''; 
                    descriptionEl.value = ''; 
                    priceEl.value = ''; 
                }
            }
        }
    });

}
