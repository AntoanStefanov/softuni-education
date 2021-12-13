function solve(input) {
    let index = 0;
    let width = Number(input[index]);
    index++;
    let height = Number(input[index]);


    let pieces = width * height;

    while (true) {
        index++;
        let data = input[index]

        if (data === 'STOP') {
            console.log(`${pieces} pieces are left.`);
            break;
        }

        let eatenPieces = Number(data);
        pieces -= eatenPieces;

        if (pieces < 0) {
            console.log(`No more cake left! You need ${Math.abs(pieces)} pieces more.`)
            break;
        }

    }
}


solve(["10",
    "10",
    "20",
    "20",
    "20",
    "20",
    "21"])

solve(["10",
    "2",
    "2",
    "4",
    "6",
    "STOP"])