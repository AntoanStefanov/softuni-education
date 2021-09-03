function solve(stockArray, delivery) {
    let stock = {};
    let product;
    let quantity;
    for (let i = 0; i < stockArray.length; i += 2) {
        product = stockArray[i];
        quantity = Number(stockArray[i + 1]);
        stock[product] = quantity
    }

    for (let i = 0; i < delivery.length; i += 2) {
        product = delivery[i];
        quantity = Number(delivery[i + 1]);
        if (product in stock) {
            stock[delivery[i]] += quantity;
        } else {
            stock[delivery[i]] = quantity;
        }
    }

    for (key in stock) {
        console.log(`${key} -> ${stock[key]}`);
    }

}


solve(
    [
        'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
        'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ]);