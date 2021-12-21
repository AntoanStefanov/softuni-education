let list = document.querySelector('#book-list ul');
list.addEventListener('click', function (event) {
    if (event.target.className === 'delete') {
        let li = event.target.parentElement;
        // li.remove();
        list.removeChild(li);
    }
});

