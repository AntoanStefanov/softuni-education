function solve(input) {
    let coins = 0;
    let change = Number(input[0]) * 100;

    while (change >= 200) {
        change -= 200;
        coins += 1;
    }

    while (change >= 100) {
        change -= 100;
        coins += 1;
    }

    while (change >= 50) {
        change -= 50;
        coins += 1;
    }

    while (change >= 20) {
        change -= 20;
        coins += 1;
    }

    while (change >= 10) {
        change -= 10;
        coins += 1;
    }

    while (change >= 5) {
        change -= 5;
        coins += 1;
    }

    while (change >= 2) {
        change -= 2;
        coins += 1;
    }

    while (change >= 1) {
        change -= 1;
        coins += 1;
    }

    console.log(coins);

}

solve(["1.23"])
solve(["2"])
solve(["0.56"])
solve(["2.73"])
