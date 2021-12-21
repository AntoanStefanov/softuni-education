function solve(arr) {
    let products = {};
    let output = {};
    for (let info of arr) {
        let [product, quantity] = info.split(' => ');
        if (!(product in products)) {
            products[product] = 0;
        }
        products[product] += +quantity;
        let bottles = Math.floor(products[product] / 1000);
        if (bottles > 0) {
            output[product] = bottles;
        }
    }

    for (let product in output) {
        console.log(`${product} => ${output[product]}`);

    }
}

solve(['Orange => 2000',
    'Peach => 1432',
    'Banana => 450',
    'Peach => 600',
    'Strawberry => 549']);

solve(['Kiwi => 234',
    'Pear => 2345',
    'Watermelon => 3456',
    'Kiwi => 4567',
    'Pear => 5678',
    'Watermelon => 6789']);