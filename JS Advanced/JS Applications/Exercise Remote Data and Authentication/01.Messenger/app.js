function attachEvents() {
    const url = 'http://localhost:3030/jsonstore/messenger';

    const textAreaEl = document.getElementById('messages');

    const refreshButton = document.getElementById('refresh');
    const sendButton = document.getElementById('submit');

    const nameInputEl = document.querySelector('input[name="author"]');
    const messageInputEl = document.querySelector('input[name="content"]');

    refreshButton.addEventListener('click', (ev) => {
        textAreaEl.textContent = 'Loading...';
        clearInputs();
        switchButtons();

        getMessages()
            .then(showMessages)
            .catch(onErrorCatch);
    });

    async function getMessages() {
        const response = await fetch(url);
        const messages = await response.json();

        return Object.values(messages);
    }

    function showMessages(messages) {
        const output = [];

        messages.forEach(({ author, content }) => {
            output.push(`${author}: ${content}`);
        })

        textAreaEl.textContent = output.join('\n');

        switchButtons();
    }

    sendButton.addEventListener('click', (ev) => {
        const author = nameInputEl.value;
        const message = messageInputEl.value;

        clearInputs();

        postMessage(author, message)
            .then(sentMessageInfo => {
                const sentBy = sentMessageInfo.author;
                const sentMessage = sentMessageInfo.content;
                textAreaEl.textContent = `${sentBy} sent message: ${sentMessage}`;
                switchButtons();
            })
            .catch(onErrorCatch);

    });

    async function postMessage(author, content) {
        textAreaEl.textContent = 'Sending...';

        switchButtons();

        if (author === '' || content === '') {
            throw new Error('Fill empty inputs');
        }

        const message = {
            author,
            content
        };

        const options = {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(message)
        };

        const response = await fetch(url, options);
        const responseBody = await response.json();

        return responseBody;
    }

    function switchButtons() {
        if (refreshButton.disabled && sendButton.disabled) {
            refreshButton.disabled = false;
            sendButton.disabled = false;
        } else {
            refreshButton.disabled = true;
            sendButton.disabled = true;
        }
    }

    function clearInputs() {
        nameInputEl.value = '';
        messageInputEl.value = '';
    }

    function onErrorCatch(err) {
        textAreaEl.textContent = 'Error: ' + err.message;
        switchButtons();
    }
}

attachEvents();