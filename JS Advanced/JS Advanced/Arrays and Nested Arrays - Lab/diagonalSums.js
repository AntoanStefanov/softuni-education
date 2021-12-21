function solve(matrix) {
    let primalDiagonal = 0;
    let secondarySum = 0;
    for (let r = 0; r < matrix.length; r++) {
        for (let c = 0; c < matrix[r].length; c++) {
            if (r === c) {
                primalDiagonal += matrix[r][c];
            }
        }
        secondarySum += matrix[r][matrix.length - r - 1];
    }
    console.log(primalDiagonal, secondarySum);
}

solve([[20, 40],
[10, 60]])

solve([[3, 5, 17],
[-1, 7, 14],
[1, -8, 89]]);