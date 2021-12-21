function solve(input) {
    let catalogue = {};
    let keys = [];
    for (let product of input) {
        product = product.split(' : ');
        catalogue[product[0]] = Number(product[1]);
        keys.push(product[0]);
    }

    // case insensitive
    keys.sort(function (a, b) {
        return a.toLowerCase().localeCompare(b.toLowerCase());
    });

    let letters = [];
    for (let key of keys) {
        let letter = key[0];
        if (!(letters.includes(letter))) {
            letters.push(letter);
        }
    }

    for (let letter of letters) {
        console.log(letter);
        for (let key of keys) {
            if (key[0] !== letter) {
                continue;
            }
            console.log(`  ${key}: ${catalogue[key]}`);

        }
    }

}

solve(['Appricot : 20.4',
    'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10']);