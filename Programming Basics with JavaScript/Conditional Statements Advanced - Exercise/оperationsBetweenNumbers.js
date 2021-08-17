function solve(input) {
    let firstNumber = Number(input[0]);
    let secondNumber = Number(input[1]);
    let operation = input[2];
    let result;
    let evenOrOdd;

    switch (operation) {
        case '+':
            result = firstNumber + secondNumber;
            if (result % 2 === 0) {
                evenOrOdd = 'even';
            } else {
                evenOrOdd = 'odd';
            }
            console.log(`${firstNumber} ${operation} ${secondNumber} = ${result} - ${evenOrOdd}`);
            break;
        case '-':
            result = firstNumber - secondNumber;
            if (result % 2 === 0) {
                evenOrOdd = 'even';
            } else {
                evenOrOdd = 'odd';
            }
            console.log(`${firstNumber} ${operation} ${secondNumber} = ${result} - ${evenOrOdd}`);
            break;
        case '*':
            result = firstNumber * secondNumber;
            if (result % 2 === 0) {
                evenOrOdd = 'even';
            } else {
                evenOrOdd = 'odd';
            }
            console.log(`${firstNumber} ${operation} ${secondNumber} = ${result} - ${evenOrOdd}`);
            break;
        case '/':
            if (secondNumber === 0) {
                console.log(`Cannot divide ${firstNumber} by zero`);
            } else {
                result = firstNumber / secondNumber;
                console.log(`${firstNumber} ${operation} ${secondNumber} = ${result.toFixed(2)}`);
            }
            break;
        case '%':
            if (secondNumber === 0) {
                console.log(`Cannot divide ${firstNumber} by zero`);
            } else {
                result = firstNumber % secondNumber;
                console.log(`${firstNumber} ${operation} ${secondNumber} = ${result}`);
            }
            break;
    }

    if (operation === '+' || operation == '-' || operation === '*') {
        
    }
}

solve(['10', '12', '+'])
solve(["10",
    "1",
    "-"]);
solve(["7",
    "3",
    "*"]);