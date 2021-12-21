array = [];

let arr = [];
let lastEl;
if (array.length % 2 !== 0) {
    lastEl = array.pop();
}
for (let i = 0; i < array.length; i += 2) {
    arr.push(array[i] + array[i + 1]);
}
if (lastEl) {
    arr.push(lastEl);
}
array = arr;