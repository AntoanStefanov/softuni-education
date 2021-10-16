// class Person {
//     constructor(firstName, lastName) {
//         this.firstName = firstName;
//         this.lastName = lastName;
//     }

//     get fullName() {
//         return this.firstName + ' ' + this.lastName;
//     }

//     set fullName(fullName) {
//         let [firstName, lastName] = fullName.split(' ');
//         this.firstName = firstName;
//         this.lastName = lastName;
//     }
// }

function createPerson(firstName, lastName) {
    let result = {
        firstName,
        lastName,
        fullName: ''
    };
    Object.defineProperty(result, 'fullName', {
        get: function () {
            return this.firstName + ' ' + this.lastName;
        },
        set: function (value) {
            let [firstName, lastName] = value.split(' ');
            this.firstName = firstName;
            this.lastName = lastName;
        },
        configurable: true,
        enumerable: true,
    });
    return result;
}

let person = createPerson("Peter", "Ivanov");
console.log(person.fullName); //Peter Ivanov
person.firstName = "George";
console.log(person.fullName); //George Ivanov
person.lastName = "Peterson";
console.log(person.fullName); //George Peterson
person.fullName = "Nikola Tesla";
console.log(person.firstName); //Nikola
console.log(person.lastName); //Tesla
