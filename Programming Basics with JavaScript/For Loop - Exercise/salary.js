function solve(input) {
    let salary = Number(input[1]);

    for (let index = 2; index < input.length; index++) {
        let web = input[index];
        if (web === 'Facebook') {
            salary -= 150;
        } else if (web === 'Instagram') {
            salary -= 100;
        } else if (web === 'Reddit') {
            salary -= 50;
        }

        if (salary <= 0) {
            console.log("You have lost your salary.")
            break;
        }
    }

    if (salary) {
        console.log(salary);
    }
}

solve(["10",
    "750",
    "Facebook",
    "Dev.bg",
    "Instagram",
    "Facebook",
    "Reddit",
    "Facebook",
    "Facebook"])