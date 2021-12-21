function toStringExtension() {
    class Person {
        constructor(name, email) {
            this.name = name;
            this.email = email;
        }

        toString() {
            return `${this.constructor.name} (name: ${this.name}, email: ${this.email})`;
        }
    }

    class Teacher extends Person {
        constructor(name, email, subject) {
            super(name, email);
            this.subject = subject;
        }

        toString() {
            let parentToString = super.toString();
            return parentToString.slice(0, -1) + `, subject: ${this.subject})`;
        }
    }

    class Student extends Person {
        constructor(name, email, course) {
            super(name, email);
            this.course = course;
        }

        toString() {
            let parentToString = super.toString();
            return parentToString.slice(0, -1) + `, course: ${this.course})`;

        }
    }

    return {
        Person,
        Teacher,
        Student
    }
}

let classes = toStringExtension();
let Person = classes.Person;
let Teacher = classes.Teacher;
let Student = classes.Student;

let person = new Person("Person", 'person@ivan.com', "prsn");
let t = new Teacher("Ivan", 'ivan@ivan.com', "Graphics");
let s = new Student("Student", 'student@ivan.com', "Std");
console.log(person.toString());
console.log(t.toString());
console.log(s.toString());