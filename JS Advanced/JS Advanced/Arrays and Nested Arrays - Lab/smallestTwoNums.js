function solve(array) {
    let firstSmallest = Math.min(...array);
    let firstSmallestIndex = array.indexOf(firstSmallest);
    array.splice(firstSmallestIndex, 1);
    let secondSmallest = Math.min(...array);
    return [firstSmallest, secondSmallest].join(' ');
}

console.log(solve([30, 15, 50, 5]));
console.log(solve([3, 0, 10, 4, 7, 3]));

