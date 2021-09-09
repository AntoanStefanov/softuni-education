function solve(number) {
    let numToString = String(number);
    let allDigitsAreSame = true;
    let sum = 0;
    for (let index = 0; index < numToString.length; index++) {
        let current = numToString[index];
        sum += +current;
        if (index + 1 == numToString.length) {
            break;
        }
        let next = numToString[index + 1];

        if (current !== next) {
            allDigitsAreSame = false;
        }
    }

    console.log(allDigitsAreSame);
    console.log(sum);
}

solve(2222222);
solve(1234);