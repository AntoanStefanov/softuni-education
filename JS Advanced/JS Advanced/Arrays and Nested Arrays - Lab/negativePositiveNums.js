function solve(array) {
    let newArray = [];

    for (let num of array) {
        if (num < 0) {
            newArray.unshift(num);
        } else {
            newArray.push(num);
        }
    }
    return newArray;
}

console.log(solve([7, -2, 8, 9]));
console.log(solve([3, -2, 0, -1]));