function solution(A) {
    let positiveNums = 0;
    let positiveNumsSum = 0;
    for (let num of A) {
        if (num > 0) {
            positiveNums++;
            positiveNumsSum += num;
        }
        if (positiveNums === 3) {
            break;
        }
    }
    return positiveNumsSum;
}

console.log(solution([4, -2, 0, 5, -2, 1, 6, 7]));
console.log(solution([3, -2, 0]));
console.log(solution([-9, -4, -2, -6]));
console.log(solution([2, 3]));



