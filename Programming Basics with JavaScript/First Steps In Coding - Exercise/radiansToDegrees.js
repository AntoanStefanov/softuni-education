function solve(input) {
    let radians = Number(input[0]);
    let degrees = radians * (180 / Math.PI);
    //  Math.round(degrees);
    let fixedDegrees = degrees.toFixed(0);
    console.log(fixedDegrees);
}

solve(['3.1416']);