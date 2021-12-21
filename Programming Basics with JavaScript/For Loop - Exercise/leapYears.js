function solve(input) {
    let firstYear = Number(input[0]);
    let secondYear = Number(input[1]);

    for (let year = firstYear; year <= secondYear; year++) {
        if ((0 == year % 4) && (0 != year % 100) || (0 == year % 400)) {
            console.log(year);
        }
    }
}

solve(['1908', '1919'])