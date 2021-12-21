function solve(array) {
    let firstEl = +array.shift();
    let lastEl = +array.pop();
    return firstEl + lastEl;
}

solve(['20', '30', '40']);