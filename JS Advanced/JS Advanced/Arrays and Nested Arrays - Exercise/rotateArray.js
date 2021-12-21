function solve(array, n) {
    for (let count = 0; count < n; count++) {
        array.unshift(array.pop());
    }

    return array.join(' ');
}

console.log(solve(['1',
    '2',
    '3',
    '4'],
    2));

console.log(solve(['Banana',
    'Orange',
    'Coconut',
    'Apple'],
    15));