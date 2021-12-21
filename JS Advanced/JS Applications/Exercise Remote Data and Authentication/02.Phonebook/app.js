function attachEvents() {
    const bodyEl = document.getElementsByTagName('body')[0];
    const phonebookURL = 'http://localhost:3030/jsonstore/phonebook/';

    const phonebookUL = document.getElementById('phonebook');

    const loadButton = document.getElementById('btnLoad');
    const createButton = document.getElementById('btnCreate');

    const personNameInput = document.getElementById('person');
    const personPhoneInput = document.getElementById('phone');

    const loadingEl = newEl('p', {}, 'Loading...');

    bodyEl.addEventListener('click', bodyOnClick);

    function bodyOnClick(ev) {
        if (ev.target.id === 'btnLoad') {
            loadButtonOnClick(ev.target);

        } else if (ev.target.id === 'btnCreate') {
            createButtonOnClick(ev.target);

        } else if (ev.target.textContent === 'Delete' ||
            ev.target.textContent.startsWith('Error:')) {
            deleteButtonOnClick(ev.target);

        } else if (ev.target.tagName === 'INPUT') {
            createButton.textContent = 'Create';
        }
    }

    function deleteButtonOnClick(button) {
        button.textContent = 'Deleting...';
        const contactID = button.id;

        deleteContact(contactID)
            .then(() => {
                button.parentElement.remove();
            })
            .catch(error => {
                button.textContent = 'Error: ' + error.message;
            });
    }

    async function deleteContact(id) {
        const contactURL = phonebookURL + id;

        const options = { method: 'DELETE' };

        const res = await fetch(contactURL, options);
        const result = await res.json();

        return result;

    }

    function loadButtonOnClick(button) {
        button.disabled = true;

        phonebookUL.replaceChildren(loadingEl);

        getAllContacts()
            .then(showPhonebook)
            .catch(error => {
                const errorMessage = 'Error: ' + error.message;
                const errorEl = newEl('p', {}, errorMessage);
                phonebookUL.replaceChildren(errorEl);
                button.disabled = false;

            });

        button.disabled = false;
    }

    function showPhonebook(phonebook) {
        formattedPhonebook = [];

        phonebook.forEach(({ person, phone, _id }) => {
            const deleteButton = newEl('button', { id: _id }, 'Delete');

            const contactInfo = `${person}: ${phone}`;

            const contact = newEl('li', {},
                contactInfo,
                deleteButton);

            formattedPhonebook.push(contact);
        });

        phonebookUL.replaceChildren(...formattedPhonebook);
    }


    function createButtonOnClick(button) {
        button.disabled = true;

        const person = personNameInput.value.trim();
        const phone = personPhoneInput.value.trim();

        personNameInput.value = '';
        personPhoneInput.value = '';

        button.textContent = 'Creating...';

        createContact(person, phone)
            .then(() => {
                loadButtonOnClick(loadButton);
                button.textContent = 'Create';
                button.disabled = false;


            })
            .catch(error => {
                button.textContent = 'Error: ' + error.message;
                button.disabled = false;
            });
    }

    async function createContact(person, phone) {

        if (person === '' || phone === '') {
            throw new Error('Fill empty inputs');
        }

        const contact = {
            person,
            phone
        };

        const options = {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(contact)
        };

        const response = await fetch(phonebookURL, options);
        const result = await response.json();

        return result;
    }

    async function getAllContacts() {

        const response = await fetch(phonebookURL);
        const phonebook = await response.json();

        return Object.values(phonebook);
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
            if (typeof item === 'string' || typeof item === 'number') {
                item = document.createTextNode(item);
            }

            element.appendChild(item);
        }

        return element;
    }
}

attachEvents();