function solve(array) {
    let health = 100;
    let coins = 0;
    let rooms = array[0].split('|');
    let room;
    let actionOrMonster;
    let amount;
    let isDead = false;
    let roomNumber = 0;

    for (let i = 0; i < rooms.length; i++) {
        room = rooms[i].split(' ');
        roomNumber++;
        actionOrMonster = room[0];
        amount = Number(room[1]);

        if (actionOrMonster == 'potion') {
            let previousHealth = health;
            let healed = amount;
            health += amount;
            if (health > 100) {
                health = 100;
                healed = 100 - previousHealth;
            }

            console.log(`You healed for ${healed} hp.`);
            console.log(`Current health: ${health} hp.`);
        } else if (actionOrMonster == 'chest') {
            coins += amount;
            console.log(`You found ${amount} coins.`);
        } else {
            health -= amount;
            if (health > 0) {
                console.log(`You slayed ${actionOrMonster}.`);
            } else {
                isDead = true;
                break;
            }
        }


    }

    if (isDead) {
        console.log(`You died! Killed by ${actionOrMonster}.`);
        console.log(`Best room: ${roomNumber}`);
    } else {
        console.log("You've made it!");
        console.log(`Coins: ${coins}`);
        console.log(`Health: ${health}`);
    }
}

solve(["rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000"]);
solve(["cat 10|potion 30|orc 10|chest 10|snake 25|chest 110"]);