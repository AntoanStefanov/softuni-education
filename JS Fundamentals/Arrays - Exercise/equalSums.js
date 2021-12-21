function solve(array) {
    let equalSums = false;

    for (let index = 0; index < array.length; index++) {
        let leftSum = 0;
        let rightSum = 0;
        for (let indexForLeft = index - 1; indexForLeft >= 0; indexForLeft--) {
            leftSum += array[indexForLeft];
        }

        for (let indexForRight = index + 1; indexForRight < array.length; indexForRight++) {
            rightSum += array[indexForRight];
        }

        if (leftSum == rightSum) {
            console.log(index);
            equalSums = true;
        }
    }

    if (!equalSums) {
        console.log('no');
    }
}

solve([1, 2, 3, 3])
solve([1, 2])
solve([1])
solve([1, 2, 3])
solve([10, 5, 5, 99, 3, 4, 2, 5, 1, 1, 4])