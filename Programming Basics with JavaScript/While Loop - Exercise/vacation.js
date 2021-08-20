function solve(input) {
    let index = 0;
    let neededMoney = Number(input[index]);
    index++;
    let currentMoney = Number(input[index]);

    let consecutiveDays = 0;
    let totalDays = 0;
    let savedSuccess = false;

    while (true) {
        totalDays++;
        index++;
        let action = input[index];
        index++;
        let amount = Number(input[index]);

        if (action === 'save') {
            consecutiveDays = 0;
            currentMoney += amount;
            if (currentMoney >= neededMoney) {
                savedSuccess = true;
                break;
            }
        } else {
            currentMoney -= amount;
            if (currentMoney < 0) {
                currentMoney = 0;
            }
            consecutiveDays++;
            if (consecutiveDays === 5) {
                break;
            }
        }
    }

    if (savedSuccess) {
        console.log(`You saved the money for ${totalDays} days.`);
    } else {
        console.log("You can't save the money.");
        console.log(`${totalDays}`);
    }

}

solve(["2000.05",
    "1000",
    "spend",
    "1200",
    "save",
    "2000"])

solve(["110",
    "60",
    "spend",
    "10",
    "spend",
    "10",
    "spend",
    "10",
    "spend",
    "10",
    "spend",
    "10",
    'spend',
    '100'])

solve(["250",
    "150",
    "spend",
    "50",
    "spend",
    "50",
    "save",
    "100",
    "save",
    "100"])
