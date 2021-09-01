function solve(array, commands) {
    let takeNumber = commands[0];
    let deleteNumber = commands[1];
    let searchNumber = commands[2];

    array.splice(takeNumber);
    array.splice(0, deleteNumber);


    let occurances = array.filter(x => x === searchNumber).length;

    console.log(`Number ${searchNumber} occurs ${occurances} times.`)
}

solve([5, 2, 3, 4, 1, 6],
    [5, 2, 3]);