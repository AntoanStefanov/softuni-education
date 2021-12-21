function solve(...args) {
    let count = {};

    for (let arg of args) {
        console.log(`${typeof arg}: ${arg}`);
        if (!(typeof arg in count)) {
            count[typeof arg] = 0;
        }
        count[typeof arg]++;
    }
    let arrToSort = [];
    for (let data of Object.entries(count)) {
        arrToSort.push(data);
    }

    arrToSort.sort(function (a, b) {
        return b[1] - a[1];
    })
    for (let data of arrToSort) {
        console.log(`${data[0]} = ${data[1]}`);
    }

}




solve('cat', 42, function () { console.log('Hello world!'); });
solve({ name: 'bob' }, 3.333, 9.999);