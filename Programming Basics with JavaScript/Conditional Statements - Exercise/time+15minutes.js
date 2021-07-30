function solve(input) {
    let hours = Number(input[0]);
    let minutes = Number(input[1]);
    let totalMinutes = hours * 60 + minutes;
    let minutesToAdd = 15;

    hours = hours % 60;
    minutes = (totalMinutes - hours * 60) + minutesToAdd;


    if (minutes > 59) {
        hours += 1;
        minutes -= 60;
    }

    if (hours > 23) {
        hours = 0;
    }

    if (minutes < 10) {
        minutes = `0${minutes}`;
    }

    console.log(`${hours}:${minutes}`);

}

solve(['11', '08'])
solve(['12', '49'])
solve(['23', '59'])

