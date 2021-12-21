class List {
    constructor() {
        this.currentList = [];
        this.size = 0;
    }


    add(element) {
        this.currentList.push(element);
        this.size++;
        if (this.size > 1) {
            this.currentList.sort((a, b) => a - b);
        }

    }

    remove(index) {
        if (this.isIndexValid(index)) {
            this.currentList.splice(index, 1);
            this.size--;

        }
    }

    get(index) {
        if (this.isIndexValid(index)) {
            return this.currentList[index];
        }
    }


    isIndexValid(index) {
        return index >= 0 && index < this.size;
    }
}



let list = new List();
list.add(5);
console.log(list.get(0));
list.add(6);
list.add(7);
console.log(list.size);
console.log(list.get(1));
list.remove(1);
console.log(list.get(1));