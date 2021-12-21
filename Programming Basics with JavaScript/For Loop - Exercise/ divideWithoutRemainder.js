function solve(input) {
    let totalNumbers = Number(input[0]);
    let firstRange = 0;
    let secondRange = 0;
    let thirdRange = 0;


    for (let index = 1; index < input.length; index++) {
        let number = Number(input[index]);
        if (number % 2 == 0) {
            firstRange += 1;
        }
        if (number % 3 == 0) {
            secondRange += 1;
        }
        if (number % 4 == 0) {
            thirdRange += 1;
        }
    }

    console.log((((firstRange / totalNumbers) * 100).toFixed(2)) + '%');
    console.log((((secondRange / totalNumbers) * 100).toFixed(2)) + '%');
    console.log((((thirdRange / totalNumbers) * 100).toFixed(2)) + '%');

}

solve(["10",
    "680",
    "2",
    "600",
    "200",
    "800",
    "799",
    "199",
    "46",
    "128",
    "65"])