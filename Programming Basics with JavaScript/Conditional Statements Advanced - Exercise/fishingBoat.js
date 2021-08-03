function solve(input) {
    let budget = Number(input[0]);
    let season = input[1];
    let numberFishers = Number(input[2]);

    let boatCost;

    if (season === 'Spring') {
        boatCost = 3000;
    } else if (season === 'Summer' || season === 'Autumn') {
        boatCost = 4200;
    } else if (season === 'Winter') {
        boatCost = 2600;
    }

    if (numberFishers >= 12) {
        boatCost *= 0.75;
    } else if (numberFishers >= 7 && numberFishers <= 11) {
        boatCost *= 0.85;
    } else {
        boatCost *= 0.90;
    }

    if (numberFishers % 2 === 0 && season !== 'Autumn') {
        boatCost *= 0.95;
    }

    let diff = Math.abs(boatCost - budget);

    if (budget >= boatCost) {
        console.log(`Yes! You have ${diff.toFixed(2)} leva left.`)
    } else {
        console.log(`Not enough money! You need ${diff.toFixed(2)} leva.`)
    }
}


solve(["3000",
    "Summer",
    "11"])

solve(["3600",
    "Autumn",
    "6"])

solve(['2000',
    'Winter',
    '13'])