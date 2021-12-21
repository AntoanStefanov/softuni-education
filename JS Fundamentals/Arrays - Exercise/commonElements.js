function solve(firstArray, secondArray) {
    let element;
    let smallestArray = firstArray;
    let largestArray = secondArray;
    if (firstArray.length > secondArray.length) {
        smallestArray = secondArray;
        largestArray = firstArray;
    }

    for (let index = 0; index < smallestArray.length; index++) {
        element = smallestArray[index];
        if (largestArray.includes(element)) {
            console.log(element);
        }
    }
}

solve(['Hey', 'hello', 2, 4, 'Peter', 'e'],
    ['Petar', 10, 'hey', 4, 'hello', '2'])

solve(['S', 'o', 'f', 't', 'U', 'n', 'i', ' '],
    ['s', 'o', 'c', 'i', 'a', 'l'])