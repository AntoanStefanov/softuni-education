function solve(input) {
    let firstSeconds = Number(input[0]);
    let secondSeconds = Number(input[1]);
    let thirdSeconds = Number(input[2]);

    let totalSeconds = firstSeconds + secondSeconds + thirdSeconds;

    let minutes = Math.floor(totalSeconds / 60);
    let seconds = (totalSeconds % 60);

    if (seconds < 10) {
        seconds = `0${seconds}`;
    }

    console.log(`${minutes}:${seconds}`);
}

solve(['35', '45', '44']);
solve(['14', '12', '10']);