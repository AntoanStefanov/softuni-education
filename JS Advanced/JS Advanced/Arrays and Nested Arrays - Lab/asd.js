function solve(matrix) {
    let pairs = 0;
    for (let r = 0; r < matrix.length; r++) {
        for (let c = 0; c < matrix[r].length; c++) {
            let element = matrix[r][c];
            if ((r + 1) < matrix.length && element === matrix[r + 1][c]) {
                pairs++;
            }
        }
    }

    console.log(pairs);
}

solve([['2', '3', '4', '7', '0'],
['4', '0', '5', '3', '4'],
['2', '3', '5', '4', '2'],
['9', '8', '7', '5', '4']]);

solve([['test', 'yes', 'yo', 'ho'],
['well', 'done', 'yo', '6'],
['not', 'done', 'yet', '5']]
);