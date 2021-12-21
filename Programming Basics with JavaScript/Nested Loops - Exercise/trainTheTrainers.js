// oprai koda

function solve(input) {
    let index = 0;
    let numberJudges = Number(input[index]);
    let presenationName;
    let grade;
    let presentationGrade;
    let totalGrade = 0;
    let finish = false;
    let numberGrades = 0;

    while (true) {

        index++;
        presenationName = input[index];
        if (presenationName === 'Finish') {
            finish = true;
            break;
        }
        presentationGrade = 0;
        for (let i = 1; i <= numberJudges; i++) {
            index++;
            grade = Number(input[index]);
            presentationGrade += grade;
            totalGrade += grade;
            numberGrades += 1;
        }

        console.log(`${presenationName} - ${(presentationGrade / numberJudges).toFixed(2)}.`);
    }
    console.log(`Student's final assessment is ${(totalGrade / numberGrades).toFixed(2)}.`);

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