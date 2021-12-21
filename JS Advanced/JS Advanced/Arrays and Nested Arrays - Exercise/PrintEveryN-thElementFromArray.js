function solve(array, n) {
    let NthElements = [];

    for (let i = 0; i < array.length; i += n) {
        NthElements.push(array[i]);
    }

    return NthElements;
}

console.log(solve(['5',
    '20',
    '31',
    '4',
    '20'],
    2));

console.log(solve(['dsa',
    'asd',
    'test',
    'tset'],
    2

));