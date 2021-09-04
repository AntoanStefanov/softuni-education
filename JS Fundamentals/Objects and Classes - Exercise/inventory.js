function solve(input) {


    class Hero {
        constructor(heroName, level, items) {
            this.heroName = heroName;
            this.level = level;
            this.items = items;
        }
    }

    let heroes = [];

    for (let heroData of input) {
        heroData = heroData.split(' / ')
        let name = heroData[0];
        let level = Number(heroData[1]);
        let items = heroData[2].split(', ');

        let hero = new Hero(name, level, items);
        heroes.push(hero);

    }

    // for 
}

solve([
    "Isacc / 25 / Apple, GravityGun",
    "Derek / 12 / BarrelVest, DestructionSword",
    "Hes / 1 / Desolator, Sentinel, Antara"
]);