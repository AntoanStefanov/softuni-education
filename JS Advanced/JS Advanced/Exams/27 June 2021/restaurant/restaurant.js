'use strict';

class Restaurant {
    constructor(budgetMoney) {
        this.budgetMoney = budgetMoney;
        this.menu = {};
        this.stockProducts = {};
        this.history = [];
    }

    get mealsCount() {
        return Object.keys(this.menu).length;
    }

    loadProducts(productsArr) {
        let actions = [];
        for (let product of productsArr) {
            let message;
            let [name, quantity, totalPrice] = product.split(' ');
            quantity = Number(quantity);
            totalPrice = Number(totalPrice);
            if (totalPrice <= this.budgetMoney) {
                this.budgetMoney -= totalPrice;
                if (!(name in this.stockProducts)) {
                    this.stockProducts[name] = 0;
                }
                this.stockProducts[name] += quantity;
                message = `Successfully loaded ${quantity} ${name}`;
            } else {
                message = `There was not enough money to load ${quantity} ${name}`;

            }
            actions.push(message);
        }
        this.history.push.apply(this.history, actions);
        return actions.join('\n');
    }

    addToMenu(meal, neededProducts, price) { // arr of "{productName} {productQuantity}" 
        if (meal in this.menu) {
            return `The ${meal} is already in the our menu, try something different.`;
        }
        let obj = {
            products: [],
            price
        };
        for (let info of neededProducts) {
            let [name, quantity] = info.split(' ');
            obj.products.push([name, +quantity]);
        }

        this.menu[meal] = obj;
        if (this.mealsCount === 1) {
            return `Great idea! Now with the ${meal} we have 1 meal in the menu, other ideas?`;
        }
        return `Great idea! Now with the ${meal} we have ${this.mealsCount} meals in the menu, other ideas?`;

    }

    showTheMenu() {
        if (this.mealsCount === 0) {
            return "Our menu is not ready yet, please come later...";
        }
        let output = [];

        for (let meal in this.menu) {
            output.push(`${meal} - $ ${this.menu[meal].price}`);
        }
        return output.join('\n');
    }

    makeTheOrder(meal) {
        if (!(meal in this.menu)) {
            return `There is not ${meal} yet in our menu, do you want to order something else?`;
        }

        let neededProducts = this.menu[meal].products;
        let mealPrice = this.menu[meal].price;
        // check if we have all needed products
        for (let [product, quantity] of neededProducts) {
            if (!(product in this.stockProducts) || this.stockProducts[product] < quantity) { // dali go ima v sklada sushtestvuva
                return `For the time being, we cannot complete your order (${meal}), we are very sorry...`;
            }
        }
        // now use it
        for (let [product, quantity] of neededProducts) {
            this.stockProducts[product] -= quantity;
        }
        this.budgetMoney += mealPrice;

        return `Your order (${meal}) will be completed in the next 30 minutes and will cost you ${mealPrice}.`;
    }
}


let kitchen = new Restaurant(1000);
kitchen.loadProducts(['Honey 50 4', 'Strawberries 20 10', 'Banana 5 1']);
kitchen.addToMenu('frozenYogurt', ['Yogurt 1', 'Honey 1', 'Banana 1', 'Strawberries 10'], 9.99);
console.log(kitchen.makeTheOrder('frozenYogurt'));