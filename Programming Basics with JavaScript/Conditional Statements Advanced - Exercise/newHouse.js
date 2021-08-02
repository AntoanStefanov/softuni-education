function solve(input) {
    let flowers = input[0];
    let numberFlowers = Number(input[1]);
    let budget = Number(input[2]);

    let cost;

    if (flowers === 'Roses') {
        cost = numberFlowers * 5;
    } else if (flowers === 'Dahlias') {
        cost = numberFlowers * 5;
    } else if (flowers === 'Tulips') {
        cost = numberFlowers * 2.80;
    } else if (flowers === 'Narcissus') {
        cost = numberFlowers * 3;
    } else if (flowers === 'Gladiolus') {
        cost = numberFlowers * 2.50;
    }
}

solve(['Roses', '55', '250'])