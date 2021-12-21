function colorize() {
    // WORKS
    // let table = document.querySelector('table');
    // let rows = Array.from(table.querySelectorAll('tr'));

    // for (let i = 1; i < rows.length; i++) {
    //     if (i % 2 !== 0) {
    //         let evenRow = rows[i];
    //         evenRow.style.background = 'teal';
    //     }
    // }
    // ***
 

    // WORKS AGAIN
    // let rows = document.querySelectorAll('table tr');
    // for (let i = 1; i < rows.length; i += 2) {
    //     let evenRow = rows[i];
    //     evenRow.style.background = 'teal';
    // }

    let evenRows = document.querySelectorAll('table tr:nth-child(even)');
    for (let row of evenRows) {
        row.style.backgroundColor = 'teal';
    }

}