function solve(commands) {
    let array = [];
    let currentNum = 1;
    for (let command of commands) {
        if (command === 'add') {
            array.push(currentNum);
        } else if (command === 'remove') {
            if (array.length > 0) {
                array.pop();
            }
        }
        currentNum++;
    }

    if (array.length > 0) {
        return array.join('\n');
    } else {
        return 'Empty';
    }

}

console.log(solve(['add',
    'add',
    'add',
    'add']));

console.log(solve(['add',
    'add',
    'remove',
    'add',
    'add']));

console.log(solve(['remove',
    'remove',
    'remove']
));