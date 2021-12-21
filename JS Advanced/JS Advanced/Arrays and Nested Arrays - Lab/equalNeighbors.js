function solve(matrix) {
    let pairs = 0;

    function isIndexValid(matrix, r, c) {
        return ((r >= 0 && r < matrix.length) && (c >= 0 && c < matrix[0].length));
    }

    function mapper(matrix, row, column, element) {
        let currentElementPairs = 0;
        map = [
            [0, 1],
            [1, 0],
        ]

        for (let direction of map) {
            possibleRow = row + direction[0];
            possibleColumn = column + direction[1];
            if (isIndexValid(matrix, possibleRow, possibleColumn)) {
                if (element === matrix[possibleRow][possibleColumn]) {
                    currentElementPairs++;
                }
            }
        }

        return currentElementPairs;

    }

    for (let r = 0; r < matrix.length; r++) {
        for (let c = 0; c < matrix[r].length; c++) {
            let element = matrix[r][c];
            let currentPairs = mapper(matrix, r, c, element)
            pairs += currentPairs;
        }
    }

    return pairs;
}

console.log(solve([
    [2, 3, 4, 7, 0],
    [4, 0, 5, 3, 4],
    [2, 3, 5, 4, 2],
    [9, 8, 7, 5, 4]
]));