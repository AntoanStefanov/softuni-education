function solve(array) {
    let NoRepeatingArray = [];
    for (let index = 0; index < array.length; index++) {
        if (!NoRepeatingArray.includes(array[index])) {
            NoRepeatingArray.push(array[index]);
        }
    }

    console.log(NoRepeatingArray.join(' '));
}

solve([1, 2, 3, 4]);
solve([7, 8, 9, 7, 2, 3, 4, 1, 2]);
solve([20, 8, 12, 13, 4, 4, 8, 5]);