function generateReport() {
    // let allCheckboxes = Array.from(document.getElementsByTagName('input'));
    // let checkedBoxes = allCheckboxes.filter(x => x.checked);
    // EQUALS TO NEXT LINE //
    let checkedBoxes = Array.from(document.querySelectorAll('input[type="checkbox"]:checked'));
    let indicesKeys = {};
    let cellsIndicesToGetFromTBody = [];
    for (let chkedBox of checkedBoxes) {
        cellsIndicesToGetFromTBody.push(chkedBox.parentElement.cellIndex);
        indicesKeys[chkedBox.parentElement.cellIndex] = chkedBox.name;
    }

    let allTRs = document.querySelectorAll('tbody tr');

    let objects = [];

    for (let tr of allTRs) {
        let cells = tr.cells;
        let currentObject = {};
        for (let index = 0; index < cells.length; index++) {
            if (cellsIndicesToGetFromTBody.includes(index)) {
                currentObject[indicesKeys[index]] = cells[index].textContent;
            }
        }
        objects.push(currentObject);
    }

    document.getElementById('output').textContent = JSON.stringify(objects, null, 2);
}