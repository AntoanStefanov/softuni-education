class ChristmasDinner {
    constructor(budget) {
        this.budget = budget;
        this.dishes = [];
        this.products = [];
        this.guests = {};
    }

    get budget() {
        return this._budget;
    }
    set budget(value) {
        if (value < 0) {
            throw new Error("The budget cannot be a negative number");
        }
        this._budget = value;
    }

    shopping(product) { // product =  [ime: price]
        let [name, price] = product;
        if (price > this.budget) {
            throw new Error("Not enough money to buy this product");
        }
        this.products.push(name); // a broika na dadeniq produkt ?
        this.budget -= price;
        return `You have successfully bought ${name}!`;
    }

    recipes(recipeObject) { // {recipeName: '...', productsList: [...]}
        let neededProducts = recipeObject.productsList;
        let allGood = neededProducts.every(element => this.products.includes(element));
        if (allGood) {
            this.dishes.push(recipeObject);
            return `${recipeObject.recipeName} has been successfully cooked!`;
        }
        throw new Error("We do not have this product");
    }

    inviteGuests(name, dish) {
        let doesDishExists = this.dishes.some(item => item.recipeName === dish);

        if (!doesDishExists) {
            throw new Error("We do not have this dish");
        }
        if (name in this.guests) {
            throw new Error("This guest has already been invited");
        }
        let obj = {};
        obj[name] = dish;
        Object.assign(this.guests, obj);
        return `You have successfully invited ${name}!`;
    }

    showAttendance() {
        let output = [];
        for (const [guest, dish] of Object.entries(this.guests)) {
            output.push(`${guest} will eat ${dish}, which consists of ${this.dishes.find(el => el.recipeName === dish).productsList.join(", ")}`)
        }

        return output.join('\n');
    }

}


let dinner = new ChristmasDinner(300);

dinner.shopping(['Salt', 1]);
dinner.shopping(['Beans', 3]);
dinner.shopping(['Cabbage', 4]);
dinner.shopping(['Rice', 2]);
dinner.shopping(['Savory', 1]);
dinner.shopping(['Peppers', 1]);
dinner.shopping(['Fruits', 40]);
dinner.shopping(['Honey', 10]);

dinner.recipes({
    recipeName: 'Oshav',
    productsList: ['Fruits', 'Honey']
});
dinner.recipes({
    recipeName: 'Folded cabbage leaves filled with rice',
    productsList: ['Cabbage', 'Rice', 'Salt', 'Savory']
});
dinner.recipes({
    recipeName: 'Peppers filled with beans',
    productsList: ['Beans', 'Peppers', 'Salt']
});

dinner.inviteGuests('Ivan', 'Oshav');
dinner.inviteGuests('Petar', 'Folded cabbage leaves filled with rice');
dinner.inviteGuests('Georgi', 'Peppers filled with beans');

console.log(dinner.showAttendance());