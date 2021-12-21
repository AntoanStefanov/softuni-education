class Company {
    constructor() {
        this.departments = {};
    }

    addEmployee(name, salary, position, department) {
        if (!name || !salary || !position || !department || salary < 0) {
            throw new Error("Invalid input!");
        }

        if (!(department in this.departments)) {
            this.departments[department] = [];
        }
        this.departments[department].push([name, salary, position]);
        return `New employee is hired. Name: ${name}. Position: ${position}`;
    }

    static compareTo(a, b) {
        let salaryA = a[1];
        let salaryB = b[1];

        if (salaryA < salaryB) { // descending
            return 1;
        } else if (salaryA > salaryB) {
            return -1;
        } else { // salaryA == salaryB // ascending
            let nameA = a[0];
            let nameB = b[0];
            return nameA.localeCompare(nameB);


        }
    }
    // static ?
    bestDepartment() {
        let bestDepartment;
        let averageSalary;
        let employeesInBestDepartment;

        for (let department in this.departments) {
            let totalSalary = 0;
            let employees = this.departments[department];
            for (let employee of employees) {
                totalSalary += employee[1];
            }
            let currentAverageSalary = totalSalary / employees.length;
            if (averageSalary === undefined || currentAverageSalary > averageSalary) {
                averageSalary = currentAverageSalary;
                bestDepartment = department;
                employeesInBestDepartment = this.departments[department];
            }
        }
        let info = [`Best Department is: ${bestDepartment}`, `Average salary: ${averageSalary.toFixed(2)}`];
        employeesInBestDepartment.sort(Company.compareTo);
        for (let employee of employeesInBestDepartment) {
            info.push(`${employee[0]} ${employee[1]} ${employee[2]}`);
        }

        return info.join("\n");
    }
}


let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer", "Construction");
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());
