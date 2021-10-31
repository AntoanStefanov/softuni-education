function solve(input) {


    class Hero {
        constructor(heroName, level, items) {
            this.heroName = heroName;
            this.level = level;
            this.items = items;
        }

        representation() {
            //  this.items.sort(); ////////
            return `Hero: ${this.heroName}\nlevel => ${this.level}\nitems => ${this.items.join(', ')}`;
        }
    }

    let heroes = [];

    for (let heroData of input) {
        let data = heroData.split(' / ')
        let name = data[0];
        let level = Number(data[1]);
        let items = data[2].split(', ');
        let hero = new Hero(name, level, items);
        heroes.push(hero);

    }

    heroes.sort((a, b) => a.level - b.level);

    for (let hero of heroes) {
        hero.items.sort();
        console.log(hero.representation());
    }
}

solve([
    "Isacc / 25 / Apple, GravityGun",
    "Derek / 12 / BarrelVest, DestructionSword",
    "Hes / 1 / Desolator, Sentinel, Antara"
]);