function solve(input) {
    let badGrades = 0;
    let index = 0;
    let totalGrade = 0;
    let totalTasks = 0;
    let lastTask;
    let threshold = Number(input[index]);
    let needBreak = false;




    while (true) {
        index++;
        let taskName = input[index];
        index++;
        let grade = Number(input[index]);

        if (taskName === 'Enough') {
            break;
        } else if (badGrades === threshold) {
            needBreak = true;
            break;
        }

        if (grade <= 4) {
            badGrades++;
        }

        totalGrade += grade;
        totalTasks++;

        lastTask = taskName;
    }

    if (needBreak) {
        console.log(`You need a break, ${badGrades} poor grades.`);
    } else {
        console.log(`Average score: ${(totalGrade / totalTasks).toFixed(2)}`);
        console.log(`Number of problems: ${totalTasks}`);
        console.log(`Last problem: ${lastTask}`);
    }
}


solve(["3",
    "Money",
    "6",
    "Story",
    "4",
    "Spring Time",
    "5",
    "Bus",
    "6",
    "Enough"])

solve(["2",
    "Income",
    "3",
    "Game Info",
    "6",
    "Best Player",
    "4"])