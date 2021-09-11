function solve(x1, y1, x2, y2) {
    let distanceBetweenFirstPointAndMiddle = Math.sqrt((x1 ** 2) + (y1 ** 2));
    let distanceBetweenSecondPointAndMiddle = Math.sqrt((x2 ** 2) + (y2 ** 2));
    let distanceBetweenTwoPoints = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);

    let validDistanceBetweenFirstPointAndMiddle = Number.isInteger(distanceBetweenFirstPointAndMiddle);
    if ((distanceBetweenFirstPointAndMiddle === parseInt(distanceBetweenFirstPointAndMiddle, 10))) {
        console.log(`{${x1}, ${y1}} to {0, 0} is valid`);
    } else {
        console.log(`{${x1}, ${y1}} to {0, 0} is invalid`);
    }

    let validDistanceBetweenSecondPointAndMiddle = Number.isInteger(distanceBetweenSecondPointAndMiddle);
    if ((distanceBetweenSecondPointAndMiddle === parseInt(distanceBetweenSecondPointAndMiddle, 10))) {
        console.log(`{${x2}, ${y2}} to {0, 0} is valid`);
    } else {
        console.log(`{${x2}, ${y2}} to {0, 0} is invalid`);
    }

    let validDistanceBetweenTwoPoints = Number.isInteger(distanceBetweenTwoPoints);
    if ((distanceBetweenTwoPoints === parseInt(distanceBetweenTwoPoints, 10))) {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
    } else {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);

    }
}

solve(3, 0, 0, 4);
solve(2, 1, 1, 1);
