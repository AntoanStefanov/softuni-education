function solve(array) {
    let products = {};
    for (let data of array) {
        let [city, product, price] = data.split(' | ')
        price = +price;
        if (!(product in products)) {
            products[product] = [];
            products[product].push([city, price]);
        } else {
            let doesCityExists = false;
            for (let info of products[product]) {
                if (info[0] === city) {
                    info[1] = price;
                    doesCityExists = true;
                    break;
                }
            }
            if (!doesCityExists) {
                products[product].push([city, price]);
            }
        }


    }
    let lowestPrice;
    let town;
    for (let product in products) {
        for (data of products[product]) {
            if (lowestPrice === undefined || data[1] < lowestPrice) {
                lowestPrice = data[1];
                town = data[0];
            }
        }
        console.log(`${product} -> ${lowestPrice} (${town})`);
        lowestPrice = undefined;
    }
}


solve(['Sample Town | Sample Product | 1000',
    'Sample Town | Orange | 2',
    'Sample Town | Peach | 1',
    'Sofia | Orange | 3',
    'Sofia | Peach | 2',
    'New York | Sample Product | 1000.1',
    'New York | Burger | 10']);

solve(['Sofia City | Audi | 100000',
    'Sofia City | BMW | 100000',
    'Sofia City | Mitsubishi | 10000',
    'Sofia City | Mercedes | 10000',
    'Sofia City | NoOffenseToCarLovers | 0',
    'Mexico City | Audi | 1000',
    'Mexico City | BMW | 99999',
    'New York City | Mitsubishi | 10000',
    'New York City | Mitsubishi | 1000',
    'Mexico City | Audi | 100000',
    'Washington City | Mercedes | 1000']);