function solve(input) {
    let firstNumber = Number(input[0]);
    let secondNumber = Number(input[1]);
    let evenSum;
    let oddSum;
    let currentNumber;
    let specialNumbers = [];


    for (let i = firstNumber; i <= secondNumber; i++) {
        evenSum = 0;
        oddSum = 0;
        numberString = i.toString();
        for (let index = 0; index < numberString.length; index++) {
            currentNumber = Number(numberString[index]);
            if (index % 2 === 0) {
                oddSum += currentNumber;
            } else {
                evenSum += currentNumber;
            }
        }

        if (evenSum === oddSum) {
            specialNumbers.push(numberString);
        }
    }

    console.log(specialNumbers.join(' '));
}

solve(["100000",
    "100050"])

solve(["123456",
    "124000"])