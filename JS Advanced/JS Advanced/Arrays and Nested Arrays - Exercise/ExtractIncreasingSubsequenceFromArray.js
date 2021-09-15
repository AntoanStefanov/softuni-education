function solve(array) {
    let sequence = [array[0]];
    array.reduce((previous, current) => {
        if (current >= previous) {
            sequence.push(current);
        }
        return current;
    })

    return sequence;
}

console.log(solve([1,
    3,
    8,
    4,
    10,
    12,
    3,
    2,
    24]));