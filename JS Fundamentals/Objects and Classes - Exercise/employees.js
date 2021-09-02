function solve(array) {
    class Employee {
        constructor(name) {
            this.name = name;
            this.personalNumber = name.length;
        }
    }
    let employees = [];
    for (let i = 0; i < array.length; i++) {
        employ = new Employee(array[i]);
        employees.push(employ);
    }

    for (let i = 0; i < employees.length; i++) {
        employ = employees[i];
        console.log(`Name: ${employ.name} -- Personal Number: ${employ.personalNumber}`);
    }
}

solve([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
])
