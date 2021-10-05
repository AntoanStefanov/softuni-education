function solve() {
    let onScreenButton = document.querySelector('#container button');
    let clearButton = document.querySelector('#archive button');
    let listWithMoviesElement = document.querySelector('#movies ul');
    let movieNameEl = document.querySelector('#container input[type="text"][placeholder="Name"]');
    let hallNameEl = document.querySelector('#container input[type="text"][placeholder="Hall"]');
    let ticketPriceEl = document.querySelector('#container input[type="text"][placeholder="Ticket Price"]');
    let listWithArchiveMoviesEl = document.querySelector('#archive ul');



    clearButton.addEventListener('click', function (e) {
        e.target.previousElementSibling.innerHTML = '';
    })

    listWithArchiveMoviesEl.addEventListener('click', function (e) {
        if (e.target.tagName === 'BUTTON' && e.target.textContent === 'Delete') {
            e.target.parentElement.remove();
        }
    })

    listWithMoviesElement.addEventListener('click', function (e) {
        if (e.target.tagName === 'BUTTON' && e.target.textContent === 'Archive') {
            let ticketsNumber = e.target.parentElement.querySelector('input').value;
            if (ticketsNumber != "" && !isNaN(Number(ticketsNumber))) {
                let ticketPrice = +(e.target.parentElement.querySelector('strong').textContent);
                let name = e.target.parentElement.parentElement.querySelector('span').textContent;
                // let hall = e.target.parentElement.parentElement.querySelector('strong').textContent;


                let liArchiveEl = document.createElement('li');
                let spanArchiveEl = document.createElement('span');
                spanArchiveEl.textContent = name;
                liArchiveEl.appendChild(spanArchiveEl);
                let strongArchiveEl = document.createElement('strong');
                strongArchiveEl.textContent = `Total amount: ${(ticketPrice * ticketsNumber).toFixed(2)}`;
                liArchiveEl.appendChild(strongArchiveEl);
                let buttonArchiveEl = document.createElement('button');
                buttonArchiveEl.textContent = 'Delete';
                liArchiveEl.appendChild(buttonArchiveEl);

                listWithArchiveMoviesEl.appendChild(liArchiveEl);
                listWithMoviesElement.removeChild(e.target.parentElement.parentElement);
            }
        }
    })


    onScreenButton.addEventListener('click', function (e) {
        e.preventDefault() // bez tova vsichko se resetva bez prichina ??


        let movieName = movieNameEl.value;
        let hallName = hallNameEl.value;
        let ticketPrice = ticketPriceEl.value;

        movieNameEl.value = '';
        hallNameEl.value = '';
        ticketPriceEl.value = '';



        if (movieName !== '' && hallName !== '' && ticketPrice !== '' && !isNaN(Number(ticketPrice))) {
            ticketPrice = Number(ticketPrice);
            if (ticketPrice === ticketPrice) { // NaN Since NaN is the only JavaScript value that is treated as unequal to itself,
                // you can always test if a value is NaN by checking it for equality to itself:
                ticketPrice = +ticketPrice;
                let liElement = document.createElement('li');
                let spanEl = document.createElement('span');
                spanEl.textContent = movieName;
                let strongEl = document.createElement('strong');
                strongEl.textContent = `Hall: ${hallName}`;
                liElement.appendChild(spanEl);
                liElement.appendChild(strongEl);

                let divEl = document.createElement('div');
                let secondStrongEl = document.createElement('strong');
                secondStrongEl.textContent = `${ticketPrice.toFixed(2)}`;
                divEl.appendChild(secondStrongEl);
                let inputEl = document.createElement('input');
                inputEl.setAttribute('placeholder', "Tickets Sold");
                divEl.appendChild(inputEl);
                let archiveButton = document.createElement('button');
                archiveButton.textContent = 'Archive';
                divEl.appendChild(archiveButton);
                liElement.appendChild(divEl);
                listWithMoviesElement.appendChild(liElement);
            }
        }
    })
}