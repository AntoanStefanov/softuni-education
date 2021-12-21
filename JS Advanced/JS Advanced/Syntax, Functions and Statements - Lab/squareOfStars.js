function solve(n) {
    for (let currentNum = 0; currentNum < n; currentNum++) {
        let row = [];
        for (let currentNum = 0; currentNum < n; currentNum++) {
            row.push('*');
        }
        console.log(row.join(' '));
    }
}

solve(1)
solve(2)
