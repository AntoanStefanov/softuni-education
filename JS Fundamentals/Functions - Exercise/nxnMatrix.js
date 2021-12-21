function solve(number) {
    let matrix = [];

    for (row = 0; row < number; row++) {
        matrix.push([]);
        for (col = 0; col < number; col++) {
            matrix[row][col] = number;
        }
    }

    for (index = 0; index < matrix.length; index++) {
        console.log(matrix[index].join(' '));
    }
}

solve(3);