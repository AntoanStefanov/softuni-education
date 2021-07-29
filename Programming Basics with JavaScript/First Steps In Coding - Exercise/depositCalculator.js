function solve(input) {
    const depositedSum = Number(input[0]);
    const dueTimeDepositedSum = Number(input[1]);
    const rate = Number(input[2]);

    const rateCollected = depositedSum * rate / 100;
    const rateForOneMonth = rateCollected / 12;
    const totalSum = depositedSum + (dueTimeDepositedSum * rateForOneMonth);
    console.log(totalSum);
}

solve(['200', '3', '5.7'])
solve(['2350', '6', '7'])