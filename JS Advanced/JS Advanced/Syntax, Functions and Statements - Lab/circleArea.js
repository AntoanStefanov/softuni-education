function solve(x) {
    let type = typeof x;

    if (type == 'number') {
        console.log((x * x * Math.PI).toFixed(2));
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${type}.`)
    }
}

solve(5);
solve('name');
