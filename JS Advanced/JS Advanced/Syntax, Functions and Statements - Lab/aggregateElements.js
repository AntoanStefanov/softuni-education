function solve(arr) {
    let sum = 0;
    let concatenatedArr = '';
    let inverseValuesSum = 0;
    for (let num of arr) {
        sum += num;
        concatenatedArr += `${num}`;
        inverseValuesSum += 1 / num;
    }
    console.log(sum);
    console.log(inverseValuesSum);
    console.log(concatenatedArr);

}

solve([1, 2, 3]);
solve([2, 4, 8, 16]);