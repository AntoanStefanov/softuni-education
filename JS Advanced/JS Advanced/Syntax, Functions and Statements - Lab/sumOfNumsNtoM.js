function solve(x, y) {
    x = +x;
    y = +y;
    let sum = 0;
    for (let currentNum = x; currentNum <= y; currentNum++) {
        sum += currentNum;
    }
    console.log(sum);
}

solve('1', '5');