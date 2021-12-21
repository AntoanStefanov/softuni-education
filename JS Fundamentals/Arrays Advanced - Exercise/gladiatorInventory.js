function solve(commands) {
    let inventory = commands[0].split(' ');

    for (let i = 1; i < commands.length; i++) {
        let command = commands[i].split(' ');
        let action = command[0];
        let equipment = command[1];

        if (action == 'Buy') {
            if (!inventory.includes(equipment)) {
                inventory.push(equipment);
            }
        } else if (action == 'Trash') {
            if (inventory.includes(equipment)) {
                let index = inventory.indexOf(equipment);
                inventory.splice(index, 1);
            }
        } else if (action == 'Repair') {
            if (inventory.includes(equipment)) {
                let index = inventory.indexOf(equipment);
                equipment = inventory.splice(index, 1)[0];
                inventory.push(equipment);
            }
        } else if (action == 'Upgrade') {
            let data = equipment.split('-');
            equipment = data[0];
            let upgrade = data[1];

            if (inventory.includes(equipment)) {
                let index = inventory.indexOf(equipment);
                inventory.splice(index + 1, 0, `${equipment}:${upgrade}`);

            }
        }
    }

    console.log(inventory.join(' '));
}

solve(['SWORD Shield Spear',
    'Buy Bag',
    'Trash Shield',
    'Repair Spear',
    'Upgrade SWORD-Steel']);

solve(['SWORD Shield Spear',
    'Trash Bow',
    'Repair Shield',
    'Upgrade Helmet-V']);