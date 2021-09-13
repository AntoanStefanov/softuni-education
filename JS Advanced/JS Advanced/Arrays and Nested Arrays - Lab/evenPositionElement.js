function solve(array) {
    let elementsOnEvenPositions = [];
    for (let i = 0; i < array.length; i++) {
        if (i % 2 == 0) {
            elementsOnEvenPositions.push(array[i]);
        }
    }

    console.log(elementsOnEvenPositions.join(" "));
}

solve(['20', '30', '40', '50', '60']);