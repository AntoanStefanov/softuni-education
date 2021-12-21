function solution() {
    let giftNameInputElement = document.querySelector('input[type="text"][placeholder="Gift name"]');
    let addButton = giftNameInputElement.nextElementSibling;

    let listOfGifts = document.querySelector('section:nth-child(2) > ul');
    let sentGifts = document.querySelector('section:nth-child(3) > ul');
    let discardedGifts = document.querySelector('section:nth-child(4) > ul');

    function addButtonOnClick(e) {
        let giftName = giftNameInputElement.value;
        giftNameInputElement.value = '';

        let gift = newEl('li', { class: 'gift' }, giftName,
            newEl('button', { id: 'sendButton' }, 'Send'),
            newEl('button', { id: 'discardButton' }, 'Discard'),
        );
        listOfGifts.appendChild(gift);
        let sendButton = gift.querySelector('#sendButton');
        sendButton.addEventListener('click', function (e) {
            let item = sendButton.parentElement;
            while (item.firstElementChild) {
                item.removeChild(item.lastChild);
            }
            sentGifts.appendChild(item);
        });
        let discardButton = gift.querySelector('#discardButton');
        discardButton.addEventListener('click', function (e) {
            let item = discardButton.parentElement;
            while (item.firstElementChild) {
                item.removeChild(item.lastChild);
            }
            discardedGifts.appendChild(item);
        });

        sortOLorUL(listOfGifts);

    }

    function sortOLorUL(OLorUL) {
        let LIS = Array.from(OLorUL.children);
        function compare(liOne, liTwo) {
            return liOne.textContent.localeCompare(liTwo.textContent);
        }
        LIS.sort(compare);
        OLorUL.innerHTML = '';
        for (let li of LIS) {
            OLorUL.appendChild(li);
        }
    }

    function newEl(type, attr, ...content) {
        const element = document.createElement(type);

        for (const prop in attr) {
            if (prop === 'class') {
                let classes = attr[prop].split(' ');
                for (let cls of classes) {
                    element.classList.add(cls);
                }
            } else {
                element.setAttribute(prop, attr[prop]);
            }
        }

        for (let item of content) {
            if (typeof item == 'string' || typeof item == 'number') {
                item = document.createTextNode(item);
            }

            element.appendChild(item);
        }

        return element;
    }

    addButton.addEventListener('click', addButtonOnClick);
}