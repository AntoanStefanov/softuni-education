function solve(input) {
    let parkingLot = [];

    for (let arr of input) {
        arr = arr.split(', ')
        let direction = arr[0];
        let carPlate = arr[1];
        if (direction === 'IN') {
            if (!(parkingLot.includes(carPlate))) {
                parkingLot.push(carPlate);
            }
        } else {
            if (parkingLot.includes(carPlate)) {
                let index = parkingLot.indexOf(carPlate);
                parkingLot.splice(index, 1);
            }
        }

    }
    if (parkingLot.length === 0) {
        console.log("Parking Lot is Empty");
    } else {
        parkingLot.sort();
        console.log(parkingLot.join('\n'));
    }
    // function comparer(a, b) {
    //     let aPlate = +a.slice(2, -2);
    //     let bPlate = +b.slice(2, -2);

    //     return aPlate - bPlate;
    // }
}

solve(['IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'IN, CA9999TT',
    'IN, CA2866HI',
    'OUT, CA1234TA',
    'IN, CA2844AA',
    'OUT, CA2866HI',
    'IN, CA9876HH',
    'IN, CA2822UU']);