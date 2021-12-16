// Write a function:

// function solution(A);

// that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

// For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

// Given A = [1, 2, 3], the function should return 4.

// Given A = [−1, −3], the function should return 1.

// Write an efficient algorithm for the following assumptions:

// N is an integer within the range [1..100,000];
// each element of array A is an integer within the range [−1,000,000..1,000,000].


function solution(A) {
    let set = new Set();
    for (let a of A) {
        if (a > 0) {
            set.add(a);
        }
    }
    for (let i = 1; i <= A.length + 1; i++) {
        if (!set.has(i)) {
            return i;
        }
    }
}

console.log(solution([1, 3, 6, 4, 1, 2]));
console.log(solution([1, 2, 3]));
console.log(solution([-3, -100]));
console.log(solution([1000, 999]));
console.log(solution([1001, 999, -1]));

console.log(solution([-3, -2, -100]));
console.log(solution([-1, 2]));
console.log(solution([]));
console.log(solution([2]));
console.log(solution([0]));
console.log(solution([-2]));






solution([-1, -3]);