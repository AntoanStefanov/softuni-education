function sortArray(arr, way) {
    function ways() {
        return {
            'asc': (a, b) => a - b,
            'desc': (a, b) => b - a,
        };
    }

    let x = ways();
    arr.sort(x[way]);
    return arr;

}

console.log(sortArray([14, 7, 17, 6, 8], 'asc'))
console.log(sortArray([14, 7, 17, 6, 8], 'desc'))