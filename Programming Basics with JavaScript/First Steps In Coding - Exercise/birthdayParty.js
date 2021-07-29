function solve(input) {
    const rent = Number(input[0]);
    const cake = rent * 0.20;
    const drinks = cake - (cake * 0.45);
    const clown = rent / 3;
    const totalCost = rent + cake + drinks + clown;
    console.log(totalCost);
}

solve(['2250']);