function solve(startingYield) {
    let totalYield = 0;
    let days = 0;
    while (startingYield >= 100) {
        days++;
        totalYield += startingYield;
        startingYield -= 10;
        totalYield -= 26; //consumation
    }
    if (totalYield >= 26) {
        totalYield -= 26;
    }
    console.log(days);
    console.log(totalYield);
}

solve(111);