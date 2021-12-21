// let arr = [30, 50, 40, 10, 70];
// let reducer = (accumulator, currentValue, index) => {
//     // accumulator += currentValue;
//     // if (index + 1 === arr.length) {
//     //     return accumulator / (index + 1);
//     // }
//     // return accumulator;

//     // or // 

//     return accumulator + (currentValue / arr.length);
// };
// console.log(arr.reduce(reducer, 0));

// let jaggedMatrix = [
//     [4, 6, 3, 0],
//     [2, 1, -2],
//     [-5, 17],
//     [7, 3, 9, 12]
// ]

// for (let row = 0; row < jaggedMatrix.length; row++) {
//     console.log(jaggedMatrix[row]);
//     for (let column = 0; column < jaggedMatrix[row].length; column++) {
//         console.log(jaggedMatrix[row][column]);
//     }
// }

const target = { a: 1, b: 2 };
const source = { b: 4, c: 5 };
console.log(target);
Object.assign(target, source);

console.log(target);
// expected output: Object { a: 1, b: 4, c: 5 }