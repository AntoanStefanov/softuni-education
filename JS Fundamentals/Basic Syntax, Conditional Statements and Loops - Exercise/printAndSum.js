function solve(firstNumber, secondNumber) {
    let numbers = [];
    let sum = 0;
    for (let currentNumber = firstNumber; currentNumber <= secondNumber; currentNumber++) {
        numbers.push(currentNumber);
        sum += currentNumber;
    }

    console.log(numbers.join(' '));
    console.log(`Sum: ${sum}`);

}

solve(5, 10)