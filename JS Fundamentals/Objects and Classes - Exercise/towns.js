function solve(array) {
    class Town {
        constructor(townName, latitude, longitude) {
            this.townName = townName;
            this.latitude = latitude;
            this.longitude = longitude;
        }
    }
    let towns = [];
    for (let i = 0; i < array.length; i++) {
        let [townName, latitude, longitude] = array[i].split(' | ');
        latitude = +latitude;
        longitude = +longitude;
        let town = new Town(townName, latitude.toFixed(2), longitude.toFixed(2));
        towns.push(town);
    }

    for (let i = 0; i < towns.length; i++) {
        let town = towns[i];
        // let str = JSON.stringify(town, null, 2);
        // console.log(str, typeof str);
        console.log(`{ town: '${town.townName}', latitude: '${town.latitude}', longitude: '${town.longitude}' }`);
    }

}

solve(['Sofia | 42.696552 | 23.32601',
    'Beijing | 39.913818 | 116.363625']);