function solve(input) {
    let number = Number(input[0]);
    let bonus = 0;

    if (number > 1000) {
        bonus += number * 0.10;
    } else if (number > 100) {
        bonus += number * 0.20;
    } else {
        bonus += 5;
    }

    if (number % 2 === 0) {
        bonus += 1;
    } else if (number % 5 === 0) {
        bonus += 2;
    }

    console.log(bonus);
    console.log(bonus + number);
}

solve(['20'])
solve(['120'])
