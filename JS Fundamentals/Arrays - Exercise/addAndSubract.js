function solve(array) {
    let arraySum = 0;
    let modifiedArraySum = 0;
    let modifiedArray = [];
    let number;
    for (let i = 0; i < array.length; i++) {
        number = array[i];
        arraySum += number;
        if (number % 2 == 0) {
            number += i;
        } else {
            number -= i;
        }
        modifiedArray.push(number);
        modifiedArraySum += number;
    }

    console.log(modifiedArray);
    console.log(arraySum);
    console.log(modifiedArraySum);

}

solve([5, 15, 23, 56, 35]);