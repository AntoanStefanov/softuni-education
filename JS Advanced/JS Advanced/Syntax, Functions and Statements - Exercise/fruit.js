function solve(fruit, grams, pricePerKG) {
    let KGtoBuy = grams / 1000;
    let cost = KGtoBuy * pricePerKG;
    console.log(`I need $${cost.toFixed(2)} to buy ${KGtoBuy.toFixed(2)} kilograms ${fruit}.`);
}

solve('orange', 2500, 1.80);