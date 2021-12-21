function solve() {
    const URL = 'http://localhost:3030/jsonstore/collections/books/';

    const loadButton = document.getElementById('loadBooks');
    const tableBody = document.querySelector('table tbody');

    const titleInputEl = document.querySelector('input[name="title"]');
    const authorInputEl = document.querySelector('input[name="author"]');


    const form = document.querySelector('form');
    const formTitle = document.querySelector('h3');
    const submitButton = form.lastElementChild;

    const displayUserMessage = document.createElement('p');

    form.appendChild(displayUserMessage);

    loadButton.addEventListener('click', () => {
        loadButton.disabled = true;
        tableBody.replaceChildren(newEl('p', {}, 'Loading...'));

        getBooks()
            .then(books => {
                const bookRows = [];
                books.forEach(({ id, author, title }) => {
                    bookRows.push(
                        newEl('tr', { id: id },
                            newEl('td', {}, title),
                            newEl('td', {}, author),
                            newEl('td', {},
                                newEl('button', {}, 'Edit'),
                                newEl('button', {}, 'Delete')
                            )
                        )
                    );
                });

                tableBody.replaceChildren(...bookRows);
                loadButton.disabled = false;
            })
            .catch(err => {
                const message = `Error: ${err.message}`;
                tableBody.replaceChildren(newEl('p', {}, message));
                loadButton.disabled = false;
            });
    });

    loadButton.click();

    form.addEventListener('submit', event => {
        event.preventDefault();

        if (submitButton.textContent === 'Save') {
            submitButton.disabled = true;
            displayUserMessage.textContent = 'Editing...';

            const title = titleInputEl.value.trim();
            const author = authorInputEl.value.trim();

            editBook(submitButton.id, author, title)
                .then(editedBook => {
                    loadButton.click();

                    submitButton.textContent = 'Submit';
                    formTitle.textContent = 'FORM';

                    const message = `Book edited! Title: ${editedBook.title}. Author: ${editedBook.author}`;
                    displayUserMessage.textContent = message;

                    submitButton.disabled = false;
                })
                .catch(err => {
                    const errorMessage = `Error: ${err.message}`;
                    displayUserMessage.textContent = errorMessage;
                    submitButton.disabled = false;
                });

        } else if (submitButton.textContent === 'Submit') {
            submitButton.disabled = true;
            displayUserMessage.textContent = 'Creating...';

            const title = titleInputEl.value.trim();
            const author = authorInputEl.value.trim();

            createBook(title, author)
                .then(createdBook => {
                    loadButton.click();
                    const message = `Book created! Title: ${createdBook.title}. Author: ${createdBook.author}`;
                    displayUserMessage.textContent = message;
                    submitButton.disabled = false;

                })
                .catch(err => {
                    const errorMessage = `Error: ${err.message}`;
                    displayUserMessage.textContent = errorMessage;
                    submitButton.disabled = false;
                });
        }

        titleInputEl.value = '';
        authorInputEl.value = '';

    });

    tableBody.addEventListener('click', event => {
        if (event.target.tagName === 'BUTTON') {
            const button = event.target;

            if (button.textContent === 'Edit') {
                const bookRow = button.parentElement.parentElement;
                const bookDataELs = bookRow.children;
                const bookData = Array.from(bookDataELs).slice(0, - 1);

                const [title, author] = bookData.map(bookInfo => bookInfo.textContent);
                const bookID = bookRow.id;

                submitButton.textContent = 'Save';
                formTitle.textContent = 'Edit FORM';
                displayUserMessage.textContent = 'Book to be edited';

                submitButton.id = bookID;

                titleInputEl.value = title;
                authorInputEl.value = author;

            } else if (button.textContent === 'Delete') {
                button.disabled = true;
                displayUserMessage.textContent = 'Deleting...';

                const bookRow = button.parentElement.parentElement;
                const bookID = bookRow.id;

                deleteBook(bookID)
                    .then(deletedBook => {
                        loadButton.click();
                        const message = `Book Deleted! Title: ${deletedBook.title}. Author: ${deletedBook.author}`;
                        displayUserMessage.textContent = message;
                        button.disabled = false;
                    })
                    .catch(err => {
                        const errorMessage = `Error: ${err.message}`;
                        displayUserMessage.textContent = errorMessage;
                        button.disabled = false;
                    });
            }
        }
    });

    async function createBook(title, author) {

        if (title === '' || author === '') {
            throw new Error('Fill empty input/s');
        }

        const body = {
            title,
            author
        };

        const options = {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        };

        const response = await fetch(URL, options);
        const result = await response.json();

        return result;
    }

    async function editBook(id, title, author) {
        const bookUrl = URL + id;


        if (title === '' || author === '') {
            throw new Error('Fill empty input/s');
        }

        const body = {
            author,
            title
        };

        const options = {
            method: 'put',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        }

        const response = await fetch(bookUrl, options);
        const editedBook = await response.json();

        return editedBook;
    }

    async function deleteBook(id) {
        const bookUrl = URL + id;

        const response = await fetch(bookUrl, { method: 'DELETE' });
        const result = await response.json();

        return result;
    }

    async function getBooks() {
        const response = await fetch(URL);
        const booksData = await response.json();

        const ids = Object.keys(booksData);
        const booksInfo = Object.values(booksData);

        return prepareBooksInfo(ids, booksInfo);
    }

    function prepareBooksInfo(ids, booksInfo) {
        let books = [];

        for (let index = 0; index < booksInfo.length; index++) {
            books.push({ id: ids[index], ...booksInfo[index] });
        }
        return books;
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

solve();