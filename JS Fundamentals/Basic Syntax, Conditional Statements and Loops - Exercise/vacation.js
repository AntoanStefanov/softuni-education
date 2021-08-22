function solve(people, type, d) {
    let peopleNumber = people;
    let typeOfGroup = type;
    let day = d;
    let ticketPrice;
    let totalPrice;

    if (day === 'Friday') {
        if (typeOfGroup === 'Students') {
            ticketPrice = 8.45
        } else if (typeOfGroup === 'Business') {
            ticketPrice = 10.90
        } else if (typeOfGroup === 'Regular') {
            ticketPrice = 15
        }
    } else if (day === 'Saturday') {
        if (typeOfGroup === 'Students') {
            ticketPrice = 9.80
        } else if (typeOfGroup === 'Business') {
            ticketPrice = 15.60
        } else if (typeOfGroup === 'Regular') {
            ticketPrice = 20
        }
    } else if (day === 'Sunday') {
        if (typeOfGroup === 'Students') {
            ticketPrice = 10.46
        } else if (typeOfGroup === 'Business') {
            ticketPrice = 16
        } else if (typeOfGroup === 'Regular') {
            ticketPrice = 22.50
        }
    }

    totalPrice = peopleNumber * ticketPrice;

    if (typeOfGroup === 'Students' && peopleNumber >= 30) {
        totalPrice *= 0.85;
    } else if (typeOfGroup === 'Business' && peopleNumber >= 100) {
        totalPrice = totalPrice - (10 * ticketPrice);
    } else if (typeOfGroup === 'Regular' && (peopleNumber >= 10 && peopleNumber <= 20)) {
        totalPrice *= 0.95;
    }

    console.log(`Total price: ${totalPrice.toFixed(2)}`);
}

solve(30,
    "Students",
    "Sunday")

solve(40,
    "Regular",
    "Saturday")

    