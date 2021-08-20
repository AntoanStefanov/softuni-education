// oprai koda

function solve(input) {
    let index = 0;
    let numberJudges = Number(input[index]);
    let presenationName;
    let grade;
    let totalGrade;
    let neededGrade = 0;
    let finish = false;
    let numberGrades = 0;

    while (true) {

        index++;
        presenationName = input[index];
        if (presenationName === 'Finish') {
            finish = true;
            break;
        }
        totalGrade = 0;
        for (let i = 1; i <= numberJudges; i++) {
            index++;
            grade = Number(input[index]);
            totalGrade += grade;
            neededGrade += grade;
            numberGrades += 1;
        }

        console.log(`${presenationName} - ${(totalGrade / numberJudges).toFixed(2)}.`);
    }
    console.log(`Student's final assessment is ${(neededGrade / numberGrades).toFixed(2)}.`);
    neededGrade = 0;
}


solve(["2",
    "While-Loop",
    "6.00",
    "5.50",
    "For-Loop",
    "5.84",
    "5.66",
    "Finish"])

solve(["3",
    "Arrays",
    "4.53",
    "5.23",
    "5.00",
    "Lists",
    "5.83",
    "6.00",
    "5.42",
    "Finish"])