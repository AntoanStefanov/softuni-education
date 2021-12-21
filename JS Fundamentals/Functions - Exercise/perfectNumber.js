function solve(number) {
    let divisors = [];
    for (num = 1; num <= number / 2; num++) {
        if (number % num === 0) {
            divisors.push(num);
        }
    }


    if (number === divisors.reduce((a, b) => a + b, 0)) {
        console.log('We have a perfect number!');
    } else {
        console.log("It's not so perfect.");
    }

}

solve(6);
solve(28);
solve(1236498);
