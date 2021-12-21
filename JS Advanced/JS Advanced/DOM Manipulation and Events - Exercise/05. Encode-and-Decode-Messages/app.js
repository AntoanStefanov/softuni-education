function encodeAndDecodeMessages() {
    let main = document.getElementById('main');
    main.addEventListener('click', function (e) {
        if (e.target.tagName == 'BUTTON' &&
            e.target.textContent == 'Encode and send it') {
            let textAreaElement = main.querySelector('textarea[placeholder="Write your message here..."]');
            let text = textAreaElement.value;
            textAreaElement.value = '';
            let encodedMessage = '';
            for (let char of text) {
                let encodedChar = String.fromCharCode(char.charCodeAt() + 1);
                encodedMessage += encodedChar;
            }
            let textAreaElementReciever = main.querySelector('textarea[placeholder="No messages..."]');
            textAreaElementReciever.value = encodedMessage;
        }

        if (e.target.tagName == 'BUTTON' &&
            e.target.textContent == 'Decode and read it') {
            let textAreaElementReciever = main.querySelector('textarea[placeholder="No messages..."]');
            let text = textAreaElementReciever.value;
            let decodedMessage = '';
            for (let char of text) {
                let decodedChar = String.fromCharCode(char.charCodeAt() - 1);
                decodedMessage += decodedChar;
            }
            textAreaElementReciever.value = decodedMessage;
        }


    })
}