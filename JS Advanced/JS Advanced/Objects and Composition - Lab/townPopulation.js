function solve(array) {
    let towns = {};

    for (let info of array) {
        let [town, pop] = info.split(' <-> ');
        if (!(town in towns)) {
            towns[town] = 0;
        }
        towns[town] += +pop;
    }

    for (let town in towns) {
        console.log(`${town} : ${towns[town]}`);
    }
}

solve(['Sofia <-> 1200000',
    'Montana <-> 20000',
    'New York <-> 10000000',
    'Washington <-> 2345000',
    'Las Vegas <-> 1000000']);