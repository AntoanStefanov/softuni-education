function solve(matrix) {
    let biggest;
    for (let array of matrix) {
        for (let num of array) {
            if (biggest === undefined || num > biggest) {
                biggest = num;
            }
        }
    }

    console.log(biggest);
}

solve([
    [20, 50, 10],
    [8, 33, 145],
]);

solve([
    [3, 5, 7, 12],
    [-1, 4, 33, 2],
    [8, 3, 0, 4],
]);

