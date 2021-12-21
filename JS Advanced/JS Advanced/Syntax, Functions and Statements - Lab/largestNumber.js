function solve(a, b, c) {
    let maxNum = a;

    if (b > a && b > c) {
        maxNum = b;
    }
    if (c > a && c > b) {
        maxNum = c;
    }
    console.log(`The largest number is ${maxNum}.`);
}

solve(5, -3, 16);