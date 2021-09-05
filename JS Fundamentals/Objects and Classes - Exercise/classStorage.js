class Storage {
    constructor(capacity) {
        this.capacity = capacity;
        this.storage = [];
    }

    get capacity() {
        let productsQuantity = 0;

        for (let product of this.storage) {
            productsQuantity += product.quantity;
        }
        return this._capacity - productsQuantity;
    }

    set capacity(value) {
        this._capacity = value;
    }

    get totalCost() {
        let sum = 0;
        for (let product of this.storage) {
            sum += product.price * product.quantity;
        }
        return sum;
    }

    addProduct(product) {
        if (!(product.quantity > this.capacity)) {
            this.storage.push(product);
        }
    }

    getProducts() {
        let info = [];
        for (let product of this.storage) {
            info.push(JSON.stringify(product));
        }
        return info.join('\n');
    }
}


let productOne = { name: 'Cucamber', price: 1.50, quantity: 15 };
let productTwo = { name: 'Tomato', price: 0.90, quantity: 25 };
let productThree = { name: 'Bread', price: 1.10, quantity: 8 };
let storage = new Storage(50);
storage.addProduct(productOne);
storage.addProduct(productTwo);
storage.addProduct(productThree);
console.log(storage.getProducts());
console.log(storage.capacity);
console.log(storage.totalCost);
