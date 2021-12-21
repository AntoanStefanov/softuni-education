window.addEventListener('DOMContentLoaded', () => {
    const userData = JSON.parse(sessionStorage.getItem('userData'));

    const userNAV = document.getElementById('user');
    const guestNAV = document.getElementById('guest');

    const currentUserSPAN = document.querySelector('p.email span');

    const loadButton = document.querySelector('button.load');

    const catchTemplateDIV = document.querySelector('div.catch');

    const catchesDIV = document.getElementById('catches')
    catchesDIV.replaceChildren();

    const form = document.querySelector('#addForm');
    const logOutButton = document.getElementById('logout');

    let ownerID;
    
    if (userData != null) {
        guestNAV.style.display = 'none';

        currentUserSPAN.textContent = userData.email;

        ownerID = userData.id;

        const addButton = document.querySelector('button.add');

        addButton.addEventListener('click', onAdd);

        addButton.disabled = false;

        logOutButton.addEventListener('click', onLogout);

    } else {
        userNAV.style.display = 'none';
        currentUserSPAN.textContent = 'guest';

        const addInputs = document.querySelectorAll('input');
        addInputs.forEach(input => input.disabled = true);
    }

    function onAdd(event) {
        event.preventDefault();
        event.target.textContent = 'Adding...';
        event.target.disabled = true;
        const formData = new FormData(form);

        const catchData = {
            angler: formData.get('angler'),
            weight: formData.get('weight'),
            species: formData.get('species'),
            location: formData.get('location'),
            bait: formData.get('bait'),
            captureTime: formData.get('captureTime')
        };

        addCatch(catchData)
            .then(() => loadButton.click())
            .catch(err => alert('Error: ' + err.message))
            .finally(() => {
                event.target.disabled = false;
                event.target.textContent = 'Add';
            });

        form.reset();
    }

    async function addCatch(catchData) {
        const inputs = Object.values(catchData)

        if (inputs.some(input => input === '')) {
            throw new Error('Fill empty input/s');
        }

        const URL = 'http://localhost:3030/data/catches'
        const options = {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': `${userData.token}`
            },
            body: JSON.stringify(catchData)
        };

        const response = await fetch(URL, options);

        if (response.status !== 200) {
            const err = await response.json();
            throw new Error(err.message);
        }
        const result = await response.json();

        return result;
    }

    loadButton.addEventListener('click', () => {
        loadButton.disabled = true;
        loadButton.textContent = 'Loading...';

        form.reset();
        catchesDIV.replaceChildren();

        getAllCatches()
            .then(catches => displayCatches(catches))
            .catch(error => alert('Error: ' + error.message))
            .finally(() => {
                loadButton.disabled = false;
                loadButton.textContent = 'Load';
            });
    });

    loadButton.click();

    function displayCatches(catches) {
        catches.forEach(catchInfo => {
            const catchCard = catchTemplateDIV.cloneNode(true);
            fillCatchCard(catchInfo, catchCard);
            catchesDIV.appendChild(catchCard);
        });
    }

    function fillCatchCard(catchInfo, catchCard) {

        catchCard.querySelectorAll('input')
            .forEach(input => {
                const currentInfo = input.classList.value;

                input.value = catchInfo[currentInfo];
                input.setAttribute('value', catchInfo[currentInfo]);
                input.disabled = true;
            });

        catchCard.querySelectorAll('button')
            .forEach(button => {
                button.data_id = catchInfo._id;
                button.setAttribute('data-id', catchInfo._id);

                if (ownerID !== catchInfo._ownerId) {
                    button.disabled = true;
                }
            });
    }

    async function getAllCatches() {
        const response = await fetch('http://localhost:3030/data/catches');
        const catches = await response.json();

        return catches;
    }

    function onLogout() {
        logOutButton.disabled = true;
        logout()
            .then(() => {
                sessionStorage.clear();
                window.location = './index.html';
            })
            .catch(err => alert(`Failed to log out. Error: ${err.message}`))
            .finally(() => logOutButton.disabled = false);
    }

    async function logout() {
        const url = 'http://localhost:3030/users/logout';

        const options = {
            method: 'get',
            headers: {
                'X-Authorization': `${userData.token}`
            }
        };

        const response = await fetch(url, options);

        if (response.status !== 204) {
            const err = await response.json();
            throw new Error(err.message);
        }
    }

    catchesDIV.addEventListener('click', event => {
        if (event.target.tagName === 'BUTTON' &&
            event.target.textContent === 'Delete') {

            const button = event.target;
            const catchID = button.attributes['data-id'].value;

            button.disabled = true;
            button.textContent = 'Deleting...';

            deleteCatch(catchID)
                .then(() => {
                    button.parentElement.remove();
                })
                .catch(err => alert(`Failed to log out. Error: ${err.message}`))
                .finally(() => {
                    button.disabled = false;
                    button.textContent = 'Delete';
                });

        } else if (event.target.tagName === 'BUTTON' &&
            event.target.textContent === 'Update') {

            const button = event.target;
            button.nextElementSibling.disabled = true;
            button.textContent = 'Save';

            const inputs = Array.from(button.parentElement.querySelectorAll('input'));

            inputs.forEach(input => input.disabled = false);

            alert('Update catch and save changes!');

        } else if (event.target.tagName === 'BUTTON' &&
            event.target.textContent === 'Save') {

            const button = event.target;
            const catchID = button.attributes['data-id'].value;

            button.disabled = true;
            button.textContent = 'Updating';


            const inputs = Array.from(button.parentElement.querySelectorAll('input'));

            const catchData = inputs.reduce((result, input) => {
                result[input.classList.value] = input.value;
                return result;
            }, {});


            updateCatch(catchID, catchData)
                .then(() => alert('Changes saved.'))
                .catch(err => alert(`Failed to save changes. Error: ${err.message}`))
                .finally(() => {
                    button.disabled = false;
                    button.textContent = 'Update';
                    button.nextElementSibling.disabled = false;
                    loadButton.click();
                });
        }
    });

    async function updateCatch(catchID, catchData) {
        const url = 'http://localhost:3030/data/catches/' + catchID;

        const inputs = Object.values(catchData);

        if (inputs.some(input => input === '')) {
            throw new Error('Fill empty input/s');
        }

        const options = {
            method: 'put',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': `${userData.token}`
            },
            body: JSON.stringify(catchData)
        };

        const response = await fetch(url, options);

        if (response.status !== 200) {
            const err = await response.json();
            throw new Error(err.message);
        }
        const result = await response.json();

        return result;
    }

    async function deleteCatch(catchID) {
        const url = 'http://localhost:3030/data/catches/' + catchID;

        const options = {
            method: 'delete',
            headers: {
                'X-Authorization': `${userData.token}`
            }
        };

        const response = await fetch(url, options);

        if (response.status !== 200) {
            const err = await response.json();
            throw new Error(err.message);
        }
    }
});
