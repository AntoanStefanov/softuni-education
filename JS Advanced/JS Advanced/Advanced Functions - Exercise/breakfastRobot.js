function solution() {
    let recipes = {
        'apple': { 'carbohydrate': 1, 'flavour': 2 },
        'lemonade': { 'carbohydrate': 10, 'flavour': 20 },
        'burger': { 'carbohydrate': 5, 'fat': 7, 'flavour': 3 },
        'eggs': { 'protein': 5, 'fat': 1, 'flavour': 1 },
        'turkey': { 'protein': 10, 'carbohydrate': 10, 'fat': 10, 'flavour': 10 }
    };
    let store = { 'protein': 0, 'carbohydrate': 0, 'fat': 0, 'flavour': 0 };

    function manager(input) {
        input = input.split(' ');
        if (input.includes('report')) {
            let output = [];
            for (let product in store) {
                output.push(`${product}=${store[product]}`);
            }
            return output.join(' ');
        } else if (input.includes('prepare')) {
            let productToPrepare = input[1];
            let quantityToPrepare = Number(input[2]);
            let recipeProducts = recipes[productToPrepare];
            for (let recipeProduct in recipeProducts) {
                let neededQuantity = recipeProducts[recipeProduct] * quantityToPrepare;
                if (store[recipeProduct] < neededQuantity) {
                    return `Error: not enough ${recipeProduct} in stock`;
                }
                store[recipeProduct] -= neededQuantity;
            }
            return 'Success';
        } else if (input.includes('restock')) {
            store[input[1]] += Number(input[2]);
            return 'Success';
        }

    }

    return manager;

}



let manager = solution();
// console.log(manager("restock flavour 50")); // Success 
// console.log(manager("prepare lemonade 4")); // Error: not enough carbohydrate in stock 
// console.log(manager("report"));

console.log(manager("restock flavour 50"));
console.log(manager("prepare lemonade 4 "));
console.log(manager("restock carbohydrate 10"));
console.log(manager("restock flavour 10"));
console.log(manager("prepare apple 1"));
console.log(manager("restock fat 10"));
console.log(manager("prepare burger 1"));
console.log(manager("report"));






