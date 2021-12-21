function solve(array, commands) {
    for (let i = 0; i < commands.length; i++) {
        let command = commands[i].split(' ');
        let action = command[0];

        if (action === 'add') {
            let index = Number(command[1]);
            let num = Number(command[2]);
            array.splice(index, 0, num);
        } else if (action === 'addMany') {
            let index = Number(command[1]);
            for (let j = command.length - 1; j >= 2; j--) {
                array.splice(index, 0, Number(command[j]));
            }
        } else if (action === 'contains') {
            console.log(array.indexOf(Number(command[1])));
        } else if (action === 'remove') {
            let index = Number(command[1]);
            if (index >= 0 && index < array.length) {
                array.splice(index, 1);
            }
        } else if (action === 'shift') {
            let positions = Number(command[1]);
            for (let count = 0; count < positions; count++) {
                array.push(array.shift());
            }
        } else if (action === 'sumPairs') {
            let arr = [];
            let lastEl;
            if (array.length % 2 !== 0) {
                lastEl = array.pop();
            }
            for (let i = 0; i < array.length; i += 2) {
                arr.push(array[i] + array[i + 1]);
            }
            // TUK GARMI SHOTOT lastEl moje da 0, a 0 dava false i ne se vryshta v array-a - 37 red / if(lastEl) shte vurne false na 0
            if (lastEl || lastEl === 0) { // moje i (lastEl !== undefined)
                arr.push(lastEl);
            }
            array = arr;
        } else if (action === 'print') {
            console.log(`[ ${array.join(', ')} ]`);
            break;
        }
    }
}

solve([0],
    ['sumPairs', 'print']);

// solve([1, 2, 3, 4, 5],
//     ['shift 2', 'print']);

// solve([1],
//     ['remove 1', 'print']);

// solve([1, 2, 1],
//     ["sumPairs", "sumPairs", 'sumPairs', 'sumPairs', 'sumPairs', "print"])

// solve([1, 2, 4, 5, 6, 7, 7],
//     ['sumPairs', 'print']);

// solve([1, 2, 3, 4, 5],
//     ['addMany 5 9 8 7 6 5', 'contains 15',
//         'remove 3', 'shift 1', 'print']);