function solve(number) {
    let numberString = number.toString();
    let oddSum = 0;
    let evenSum = 0;
    let currentDigit;

    for (let i = 0; i < numberString.length; i++) {
        currentDigit = Number(numberString[i]);
        if (currentDigit % 2 == 0) {
            evenSum += currentDigit;
        } else {
            oddSum += currentDigit;
        }
    }
    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
}

solve(1000435);