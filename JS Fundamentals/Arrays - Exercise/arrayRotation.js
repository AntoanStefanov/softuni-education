function solve(array, rotations) {
    let element;
    for (let rotation = 0; rotation < rotations; rotation++) {
        element = array.shift();
        array.push(element);
    }
    console.log(array.join(' '));
}

solve([51, 47, 32, 61, 21], 2);
solve([32, 21, 61, 1], 4);