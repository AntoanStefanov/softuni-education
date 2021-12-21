function solve(firstNumber, operation, secondNumber) {

    let result;
    if (operation === '+') {
        result = firstNumber + secondNumber;
    } else if (operation === '-') {
        result = firstNumber - secondNumber;
    } else if (operation === '*') {
        result = firstNumber * secondNumber;
    } else if (operation === '/') {
        if (firstNumber !== 0 && secondNumber !== 0) {
            result = firstNumber / secondNumber;
        }
    }
    if (result) {
        console.log(result.toFixed(2));
    }
}

solve(1,
    '/',
    20);