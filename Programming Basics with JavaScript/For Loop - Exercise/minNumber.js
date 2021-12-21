function solve(input) {
    let minNumber;

    for (let index = 1; index < input.length; index++) {
        let currentNumber = Number(input[index]);
        if (!minNumber || minNumber > currentNumber) {
            minNumber = currentNumber;
        }
    }
    console.log(minNumber);
}

solve(['2', '100', '99'])