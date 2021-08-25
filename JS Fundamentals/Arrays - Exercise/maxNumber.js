function solve(array) {
    let currentNum;
    let isMax = true;
    let numbers = [];
    for (let index = 0; index < array.length; index++) {
        currentNum = array[index];
        isMax = true;
        for (let i = index + 1; i < array.length; i++) {
            if (currentNum <= array[i]) {
                isMax = false;
                break;
            }
        }

        if (isMax) {
            numbers.push(currentNum);
        }

    }

    console.log(numbers.join(' '));
}

solve([2, 1])
solve([1, 4, 3, 2]);
solve([14, 24, 3, 19, 15, 17]);

// S while napravi inner loop