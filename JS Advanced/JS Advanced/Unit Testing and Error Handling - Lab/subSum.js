function solve(array, startIndex, endIndex) {
    let isArray = Array.isArray(array);
    if (!isArray) {
        return NaN;

    }
    if (startIndex < 0) {
        startIndex = 0;
    }
    if (endIndex >= array.length) {
        endIndex = array.length - 1;
    }
    let sum = 0;
    for (let i = startIndex; i <= endIndex; i++) {
        let item = Number(array[i]); // ako item-a ne e Number , to cast-a shte vurne NaN
        if (item !== item) { // NaN !== NaN, a 1 === 1
            return NaN;
        }
        sum += item;
    }
    return sum;

}



console.log(solve([10, 20, 30, 40, 50, 60], 3, 300));
console.log(solve([10, 'twenty', 30, 40], 0, 2));
console.log(solve('text', 0, 2));
console.log(solve([1.1, 2.2, 3.3, 4.4, 5.5], -3, 1));
