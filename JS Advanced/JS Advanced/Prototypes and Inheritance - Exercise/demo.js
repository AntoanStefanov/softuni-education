// const food = {
//     init: function (type) {
//         this.type = type;
//     },

//     eat: function () {
//         console.log('you ate the ' + this.type);
//     }
// }


// const waffle = Object.create(food);

// food.eat = function () {
//     console.log('YOU REALLY ATE THAT ' + this.type);
// }

// waffle.init('waffle');
// waffle.eat();



// function Person(saying) {
//     this.saying = saying;
// }

// Person.prototype.talk = function () {
//     console.log('I say ' + this.saying);
// }

// function myNew(constructor, ...args) {
//     let obj = {};
//     Object.setPrototypeOf(obj, constructor.prototype);
//     constructor.apply(obj, args);
//     return obj;
// }

// let person = myNew(Person, 'motherfucker you');
// person.talk();
// let asd = 5;



class Employee {
    constructor(name, age, tasks = [], salary = 0,) {
        this.name = name;
        this.age = age;
        this.salary = salary;
        this.tasks = tasks;
    }

    getSalary() {

    }

    currentTask() {
        let currentTaskNum = -1;
        function getCurrentTask() {
            if (currentTaskNum === this.tasks.length) {
                currentTaskNum = -1;
            }
            currentTaskNum++;
            return this.tasks[currentTaskNum];
        }
        getCurrentTask();
    }

    work() {
        console.log(this.currentTask());
    }

    collectSalary() {
        console.log(`${this.name} received ${this.salary} this month.`);
    }

}



Object.setPrototypeOf(obj, currentTask)

obj.currentTask();