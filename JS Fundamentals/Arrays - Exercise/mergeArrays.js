function solve(firstArray, secondArray) {
    let mergedArray = [];
    let firstElement;
    let secondElement;

    for (let index = 0; index < firstArray.length; index++) {
        firstElement = firstArray[index]
        secondElement = secondArray[index]

        if (index % 2 == 0) {
            firstElement = Number(firstElement);
            secondElement = Number(secondElement);
        }
        mergedArray.push(firstElement + secondElement);
    }
    console.log(mergedArray.join(' - '));
}

solve(['5', '15', '23', '56', '35'],
    ['17', '22', '87', '36', '11']);