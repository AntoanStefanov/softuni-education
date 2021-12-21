function solve(array) {
    let currentSequence;
    let longestSequence = [];
    let currentNum;
    for (let index = 0; index < array.length; index++) {
        currentSequence = [];
        currentNum = array[index];
        currentSequence.push(currentNum);
        for (let nextIndex = index + 1; nextIndex < array.length; nextIndex++) {
            if (array[nextIndex] === currentNum) {
                currentSequence.push(array[nextIndex]);
                if (currentSequence.length > longestSequence.length) {
                    longestSequence = currentSequence;
                }
            } else {
                break;
            }
        }
    }

    console.log(longestSequence.join(' '));
}

solve([2, 1, 1, 2, 3, 3, 2, 2, 2, 1])
solve([1, 1, 1, 2, 3, 1, 3, 3])
solve([4, 4, 4, 4])