function solve(array) {
    let guests = [];

    for (let i = 0; i < array.length; i++) {
        let message = array[i].split(' ');
        let name = message[0];
        if (!message.includes('not')) {
            if (!guests.includes(name)) {
                guests.push(name);
            } else {
                console.log(`${name} is already in the list!`);
            }
        } else {
            if (guests.includes(name)) {
                let index = guests.indexOf(name);
                guests.splice(index, 1);
            } else {
                console.log(`${name} is not in the list!`);
            }
        }
    }

    console.log(`${guests.join('\n')}`)
}

solve(['Allie is going!',
    'George is going!',
    'John is not going!',
    'George is not going!']);

solve(['Tom is going!',
    'Annie is going!',
    'Tom is going!',
    'Garry is going!',
    'Jerry is going!']);