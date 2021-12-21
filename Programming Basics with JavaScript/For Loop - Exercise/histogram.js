function solve(input) {
    let totalNumbers = Number(input[0]);
    let firstRange = 0;
    let secondRange = 0;
    let thirdRange = 0;
    let forthRange = 0;
    let fifthRange = 0;

    for (let index = 1; index < input.length; index++) {
        let number = Number(input[index]);
        if (number < 200) {
            firstRange += 1;
        } else if (number < 400) {
            secondRange += 1;
        } else if (number < 600) {
            thirdRange += 1;
        } else if (number < 800) {
            forthRange += 1;
        } else {
            fifthRange += 1;
        }
    }

    console.log((((firstRange / totalNumbers) * 100).toFixed(2)) + '%');
    console.log((((secondRange / totalNumbers) * 100).toFixed(2))+ '%');
    console.log((((thirdRange / totalNumbers) * 100).toFixed(2))+ '%');
    console.log((((forthRange / totalNumbers) * 100).toFixed(2))+ '%');
    console.log((((fifthRange / totalNumbers) * 100).toFixed(2))+ '%');
}

solve(["3",
    "1",
    "2",
    "999"])

solve(["7",
    "800",
    "801",
    "250",
    "199",
    "399",
    "599",
    "799"])