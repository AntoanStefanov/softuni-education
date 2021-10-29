function solve(input) {
    let index = 0;
    let goal = 10000;

    while (true) {
        let data = input[index];
        if (data === 'Going home') {
            index++;
            goal -= Number(input[index]);
            if (goal <= 0) {
                console.log('Goal reached! Good job!')
                console.log(`${Math.abs(goal)} steps over the goal!`)

            } else {
                console.log(`${goal} more steps to reach goal.`)
            }

            break;
        }
        let steps = Number(data);
        index++;
        goal -= steps;
        if (goal <= 0) {
            console.log('Goal reached! Good job!')
            console.log(`${Math.abs(goal)} steps over the goal!`)
            break;
        }
    }
}



solve(["1000",
    "1500",
    "2000",
    "6500"])

solve(["1500",
    "3000",
    "250",
    "1548",
    "2000",
    "Going home",
    "2000"])

solve(["1500",
    "300",
    "2500",
    "3000",
    "Going home",
    "200"])
