window.addEventListener('load', solve);

function solve() {
    document.getElementById('add').addEventListener('click', addArticle);

    const buttonsStatus = new Map;

    function addArticle(ev) {
        ev.preventDefault();
        const inputs = Array.from(document.querySelectorAll('form input'));
        const descriptionInput = document.querySelector('textarea');

        const model = inputs[0].value;
        const year = Number(inputs[1].value);
        const description = descriptionInput.value;
        const price = Number(inputs[2].value);

        if (model === '' || description === '' || year <= 0 || price <= 0) {
            return;
        }

        const furnitureList = document.querySelector('#furniture-list');

        const moreBtn = e('button', { class: 'moreBtn' }, 'More Info');
        buttonsStatus.set(moreBtn, false);
        moreBtn.addEventListener('click', moreInfo);

        const buyBtn = e('button', { class: 'buyBtn' }, 'Buy it');
        buyBtn.addEventListener('click', buy);

        const trInfo = e('tr', { class: 'info' },
            e('td', {}, model),
            e('td', {}, price.toFixed(2)),
            e('td', {},
                moreBtn,
                buyBtn
            )
        );

        const trHidden = e('tr', { class: 'hide' },
            e('td', {}, `Year: ${year}`),
            e('td', { colspan: '3' }, `Description: ${description}`)
        );

        furnitureList.appendChild(trInfo);
        furnitureList.appendChild(trHidden);

        inputs.forEach(i => i.value = '');
        descriptionInput.value = '';
    }

    function moreInfo(ev) {
        let nextSibling = ev.target.parentElement.parentElement.nextSibling;

        if (!buttonsStatus.get(ev.target)) {
            ev.target.textContent = 'Less Info';
            nextSibling.style.display = 'contents';
            buttonsStatus.set(ev.target, true);
        } else {
            ev.target.textContent = 'More Info';
            nextSibling.style.display = 'none';
            buttonsStatus.set(ev.target, false);
        }

    }

    function buy(ev) {
        const total = document.querySelector('tfoot td.total-price');
        const currentValue = Number(total.textContent);
        const newValue = Number(ev.target.parentElement.previousSibling.textContent) + currentValue;
        total.textContent = newValue.toFixed(2);
        ev.target.parentElement.parentElement.nextSibling.remove();
        ev.target.parentElement.parentElement.remove();

    }


    function e(type, attr, ...content) {
        const element = document.createElement(type);

        for (const prop in attr) {
            if (prop === 'class') {
                element.classList.add(attr[prop])
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
}