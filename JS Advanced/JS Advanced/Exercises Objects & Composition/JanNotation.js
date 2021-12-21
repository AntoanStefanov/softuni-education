function solve(array) {
    let numbers = [];

    for (let data of array) {
        if (typeof data === 'number') {
            numbers.push(data);
        } else {
            if (numbers.length >= 2) {
                let firstNum = numbers.pop();
                let secondNum = numbers.pop();
                numbers.push(eval(`${secondNum} ${data} ${firstNum}`));

            } else {
                return "Error: not enough operands!";
            }

        }
    }
    if (numbers.length > 1) {
        return "Error: too many operands!";
    } else {
        return numbers[0];
    }
}

solve([3,
    4,
    '+']);

solve([5,
    3,
    4,
    '*',
    '-']);