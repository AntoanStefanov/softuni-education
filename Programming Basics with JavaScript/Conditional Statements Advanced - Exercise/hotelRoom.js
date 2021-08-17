function solve(input) {
    let month = input[0];
    let nights = Number(input[1]);
    
    let pricePerNightStudio;
    let pricePerNightApartment;
    let costStudio;
    let costApartment;
    let discountStudio;
    let discountApartment;

    switch (month) {
        case 'May':
        case 'October':
            pricePerNightStudio = 50;
            pricePerNightApartment = 65;
            if (nights > 14) {
                discountStudio = 0.70;
            } else if (nights > 7) {
                discountStudio = 0.95;
            }
            break;
        case 'June':
        case 'September':
            pricePerNightStudio = 75.20;
            pricePerNightApartment = 68.70;
            if (nights > 14) {
                discountStudio = 0.80;
            }
            break;
        case 'July':
        case 'August':
            pricePerNightStudio = 76;
            pricePerNightApartment = 77;
    }

    if (nights > 14) {
        discountApartment = 0.90;
    }

    if (discountStudio) {
        costStudio = (nights * pricePerNightStudio) * discountStudio;
    } else {
        costStudio = nights * pricePerNightStudio;
    }
    if (discountApartment) {
        costApartment = (nights * pricePerNightApartment) * discountApartment;
    } else {
        costApartment = nights * pricePerNightApartment;
    }

    console.log(`Apartment: ${costApartment.toFixed(2)} lv.`)
    console.log(`Studio: ${costStudio.toFixed(2)} lv.`)
}

solve(["May", "15"]);
solve(["June", "14"]);
