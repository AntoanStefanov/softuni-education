function solve(input) {
    let heroes = [];
    for (let heroData of input) {
        let data = heroData.split(' / ')
        let name = data[0];
        let level = Number(data[1]);
        let items = data[2] ? data[2].split(', ') : [];
        let hero = {
            name: name,
            level: level,
            items: items,
        }
        heroes.push(hero);

    }

    return JSON.stringify(heroes);
}

console.log(solve(['Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara']));


console.log(solve(['Jake / 1000 / Gauss, HolidayGrenade']));