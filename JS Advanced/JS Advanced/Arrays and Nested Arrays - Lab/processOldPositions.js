function solve(array) {
    let numsAtOddIndex = [];
    for (let i = 0; i < array.length; i++) {
        if (i % 2 !== 0) {
            numsAtOddIndex.push(array[i]);
        }
    }

    let doubledNums = numsAtOddIndex.map(a => a * 2);
    return doubledNums.reverse().join(' ');
}

console.log(solve([10, 15, 20, 25]));
console.log(solve([3, 0, 10, 4, 7, 3]));
