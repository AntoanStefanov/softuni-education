function solve(a, b) {
    let min = a;
    if (b < a) {
        min = b;
    }

    for (let currentNum = min; currentNum > -1; currentNum--) {
        if (a % currentNum === 0 && b % currentNum === 0) {
            console.log(currentNum);
            break;
        }
    }
}

solve(15, 5);