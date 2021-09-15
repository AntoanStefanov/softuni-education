function solve(matrix) {
    let rowsSums = [];
    let ColsSums = [];
    for (let row = 0; row < matrix.length; row++) {
        let currentRowSum = 0;
        for (let col = 0; col < matrix[row].length; col++) {
            currentRowSum += matrix[row][col];
        }
        rowsSums.push(currentRowSum);
    }
    let isEqual;
    let currentColSum = 0;
    for (column = 0; column < matrix[0].length; column++) {
        for (let row = 0; row < matrix.length; row++) {
            currentColSum += matrix[row][column];
        }
        isEqual = rowsSums.every(rowSum => rowSum === currentColSum);
        if (!isEqual) {
            break;
        }
        currentColSum = 0;
    }
    return isEqual;
}

console.log(
    solve(
        [
            [4, 5, 6],
            [6, 5, 4],
            [5, 5, 5]
        ]
    )
);


console.log(
    solve(
        [
            [11, 32, 45],
            [21, 0, 1],
            [21, 1, 1]
        ]
    )
);

console.log(
    solve(
        [
            [1, 0, 0],
            [0, 0, 1],
            [0, 1, 0]
        ]
    )
);