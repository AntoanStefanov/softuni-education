const main = document.querySelector('main');

export function showSection(section) {
    main.replaceChildren(section);
}

export function updateUserNav() {
    const userData = JSON.parse(sessionStorage.getItem('userData'));

    if (userData !== null) {
        nav.querySelector('#welcomeMsg').textContent = `Welcome, ${userData.email}`;
        [...nav.querySelectorAll('.user')]
            .forEach(item => item.style.display = 'block');
        [...nav.querySelectorAll('.guest')]
            .forEach(item => item.style.display = 'none');
    } else {
        nav.querySelector('#welcomeMsg').textContent = `Welcome, guest`;
        [...nav.querySelectorAll('.user')]
            .forEach(item => item.style.display = 'none');
        [...nav.querySelectorAll('.guest')]
            .forEach(item => item.style.display = 'block');
    }
}

export function newEl(type, attr, ...content) {
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
