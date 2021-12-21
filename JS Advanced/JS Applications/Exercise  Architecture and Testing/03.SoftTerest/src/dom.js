const main = document.querySelector('main');

export function showSection(section) {
    main.replaceChildren(section);
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
