function solve(number) {
    let sumDigits = 0;
    let numberString = number.toString();
    for (let number of numberString) {
        sumDigits += Number(number);
    }
    console.log(sumDigits);
}

solve(245678)