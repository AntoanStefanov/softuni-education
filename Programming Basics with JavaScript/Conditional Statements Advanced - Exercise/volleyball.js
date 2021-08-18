function solve(input) {
    let yearWeekends = 48;
    let yearType = input[0];
    let holidays = Number(input[1]);
    let homeWeekends = Number(input[2]);
    let sofiaWeekends = yearWeekends - homeWeekends;

    let saturdaysGamesSofia = sofiaWeekends * (3 / 4);
    let sundaysGamesHome = homeWeekends;
    let holidaysGamesSofia = holidays * (2 / 3);
    let totalGames = saturdaysGamesSofia + sundaysGamesHome + holidaysGamesSofia;

    if (yearType === 'leap') {
        totalGames *= 1.15;
    }
    console.log(Math.floor(totalGames));
}

solve(["leap",
    "5",
    "2"])

solve(["normal",
    "3",
    "2"])