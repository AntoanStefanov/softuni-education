function deleteByEmail() {
    let email = document.getElementsByName('email')[0].value;
    let rows = document.querySelectorAll('#customers tbody tr');
    let result = document.querySelector('#result');
    let isFound = false;
    for (let row of rows) {
        let currentEmail = row.cells[1].textContent;
        if (currentEmail == email) {
            row.remove();
            result.innerHTML = 'Deleted.';
            isFound = true;
            break;
        }
    }
    if (!isFound) {
        result.innerHTML = 'Not found.';
    }
}