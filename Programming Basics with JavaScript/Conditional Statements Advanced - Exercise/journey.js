function solve(input) {
    let budget = Number(input[0]);
    let season = input[1];

    let place;
    let cost;
    let destination;

    if (season === 'summer') {
        place = 'Camp';
    } else if (season === 'winter') {
        place = 'Hotel';
    }

    if (budget <= 100) {
        destination = 'Bulgaria';
        if (season === 'summer') {
            cost = budget * 0.30;
        } else if (season === 'winter') {
            cost = budget * 0.70;
        }
    } else if (budget <= 1000) {
        destination = 'Balkans';
        if (season === 'summer') {
            cost = budget * 0.40;
        } else if (season === 'winter') {
            cost = budget * 0.80;
        }
    } else {
        destination = 'Europe';
        cost = budget * 0.90;
        place = 'Hotel';
    }

    console.log(`Somewhere in ${destination}`);
    console.log(`${place} - ${cost.toFixed(2)}`);
}

solve(["50", "summer"])
solve(["75", "winter"])
solve(["312", "summer"])

