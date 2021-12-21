function solve(input) {
    let numberString;
    let currentNum;
    let isSpecial;
    let n = Number(input[0]);
    let specialNumbers = [];

    for (let i = 1111; i <= 9999; i++) {
        numberString = i.toString();
        isSpecial = true;
        for (let j = 0; j < numberString.length; j++) {
            currentNum = Number(numberString[j]);
            if (n % currentNum !== 0) {
                isSpecial = false;
                break;
            }
        }
        if (isSpecial) {
            specialNumbers.push(numberString);
        }
    }

    console.log(specialNumbers.join(' '));
}

solve(['3'])
// solve(['11'])
// solve(['16'])
