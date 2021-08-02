function solve(input) {
    let flowers = input[0];
    let numberFlowers = Number(input[1]);
    let budget = Number(input[2]);

    let cost;

    if (flowers === 'Roses') {
        cost = numberFlowers * 5;
    } else if (flowers === 'Dahlias') {
        cost = numberFlowers * 3.80;
    } else if (flowers === 'Tulips') {
        cost = numberFlowers * 2.80;
    } else if (flowers === 'Narcissus') {
        cost = numberFlowers * 3;
    } else if (flowers === 'Gladiolus') {
        cost = numberFlowers * 2.50;
    }

    if (flowers === 'Roses' && numberFlowers > 80) {
        cost *= 0.90;
    } else if (flowers === 'Dahlias' && numberFlowers > 90) {
        cost *= 0.85;
    } else if (flowers === 'Tulips' && numberFlowers > 80) {
        cost *= 0.85;
    } else if (flowers === 'Narcissus' && numberFlowers < 120) {
        cost *= 1.15;
    } else if (flowers === 'Gladiolus' && numberFlowers < 80) {
        cost *= 1.20;
    }

    if (budget >= cost) {
        console.log(`Hey, you have a great garden with ${numberFlowers} ${flowers} and ${(budget - cost).toFixed(2)} leva left.`)
    } else {
        console.log(`Not enough money, you need ${(cost - budget).toFixed(2)} leva more.`)
    }
}

solve(['Roses', '55', '250'])
solve((["Tulips",
    "88",
    "260"]))

solve(['Dahlias',
    '112',
    '460'])