function sumTable() {
    // let priceCells = document.querySelectorAll('table tbody tr td:nth-child(even)');
    // let totalPrice = 0;
    // for (cell of priceCells) {
    //     totalPrice += +cell.textContent;
    // }
    // let sumCell = document.querySelector('#sum');
    // sumCell.textContent = totalPrice;

    // let rows = document.querySelectorAll('table tbody tr');
    // let totalSum = 0;
    // for (let i = 1; i < rows.length - 1; i++) { // bez purvi i posleden
    //     let currentRowCells = rows[i].children;
    //     let currentPriceCell = currentRowCells[currentRowCells.length - 1];
    //     let currentPrice = +currentPriceCell.textContent; // + === Number();
    //     totalSum += currentPrice;
    // }
    // document.getElementById('sum').textContent = totalSum;


    // let rows = Array.from(document.querySelectorAll('table tbody tr'));
    // rows = rows.slice(1, -1); // bez purvi i posleden
    // let totalSum = 0;
    // for (let row of rows) { 
    //     let currentRowCells = row.children;
    //     let currentPriceCell = currentRowCells[currentRowCells.length - 1];
    //     let currentPrice = +currentPriceCell.textContent; // + === Number();
    //     totalSum += currentPrice;
    // }
    // document.getElementById('sum').textContent = totalSum;



    let rows = Array.from(document.querySelectorAll('table tbody tr')).slice(1, -1);

    document.getElementById('sum').textContent = rows.reduce((sum, row) => {
        return sum + Number(row.lastElementChild.textContent);
    }, 0);
}