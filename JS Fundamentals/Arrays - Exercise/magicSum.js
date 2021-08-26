function solve(array, magicSum) {
    let sums = [];
    for (let index = 0; index < array.length; index++) {
        let currentNum = array[index];
        for (let i = index + 1; i < array.length; i++) {
            if (currentNum + array[i] === magicSum) {
                sums.push([currentNum, array[i]]);
            }
        }
    }

    for (let i = 0; i < sums.length; i++) {
        console.log(sums[i].join(' ')); // console.log(sums[i]); Doesn't print all
    }
}

solve([1, 7, 6, 2, 19, 23],
    8)

solve([14, 20, 60, 13, 7, 19, 8],
    27)

solve([1, 2, 3, 4, 5, 6],
    6)

