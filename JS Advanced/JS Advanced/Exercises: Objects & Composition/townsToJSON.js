function solve(array) {
    class Town {
        constructor(townName, latitude, longitude) {
            this.Town = townName;
            this.Latitude = latitude;
            this.Longitude = longitude;
        }
    }
    let towns = [];
    for (let i = 1; i < array.length; i++) {
        let [townName, latitude, longitude] = array[i].split(' | ');
        townName = townName.slice(2);
        latitude = +latitude;
        longitude = +longitude.slice(0, -2);
        let town = new Town(townName, +latitude.toFixed(2), +longitude.toFixed(2));
        towns.push(town);
    }

    console.log(JSON.stringify(towns));
}

solve(['| Town | Latitude | Longitude |',
    '| Sofia | 42.696552 | 23.32601 |',
    '| Beijing | 39.913818 | 116.363625 |']);