function solve(array) {
    let command;
    let value;

    let index = 0;
    let train = array[index].split(' ').map(x => Number(x));
    index++;
    let maxWagonCapacity = Number(array[index]);
    index++;
    let commands = array.slice(index);

    for (let i = 0; i < commands.length; i++) {
        command = commands[i]
        if (command.includes('Add')) {
            command = command.split(' ');
            value = Number(command[1]);
            if (value > maxWagonCapacity) {
                value = maxWagonCapacity;
            }
            train.push(value);
        } else {
            value = Number(command);


            for (let i = 0; i < train.length; i++) {
                if (!((train[i] + value) > maxWagonCapacity)) {
                    train[i] += value;
                    break;
                }
            }
        }
    }

    console.log(train.join(' '));
}

solve(['32 54 21 12 4 0 23',
    '75',
    'Add 10',
    'Add 0',
    '30',
    '10',
    '75']);