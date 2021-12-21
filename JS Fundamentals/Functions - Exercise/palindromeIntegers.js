function isPalindrome(number) {
    let backwardNumber = '';
    let numberString = number.toString()
    for (let i = numberString.length - 1; i >= 0; i--) {
        backwardNumber += (numberString[i]);
    }
    return numberString === backwardNumber;
}

function solve(array) {
    let currentNum;
    for (let i = 0; i < array.length; i++) {
        currentNum = array[i];
        console.log(isPalindrome(currentNum));
    }
}

solve([123, 323, 421, 121]);
solve([32, 2, 232, 1010]);
