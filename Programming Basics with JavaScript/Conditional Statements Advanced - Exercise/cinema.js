function solve(input) {
    let projection = input[0];
    let rows = Number(input[1]);
    let cols = Number(input[2]);
    let tickets = rows * cols;
    
    let cost;

    if (projection === 'Premiere') {
        cost = tickets * 12;
    } else if (projection === 'Normal') {
        cost = tickets * 7.5;
    } else if (projection === 'Discount') {
        cost = tickets * 5;
    }
    console.log(`${cost.toFixed(2)} leva`);
}

solve(['Premiere', '10', '12'])