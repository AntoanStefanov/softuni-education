function solve(year, month, day) {
    day--;
    if (day <= 0) {
        month--;
        if (month === 'January' || month === 'March' || month === 'May' || month === 'July' || month === 'August' || month === 'October' || month === 'December') {
            day = 31;
        } else if (month === 'February') {
            day = 29;
        } else {
            day = 30;
        }

        if (month <= 0) {
            year--;
            month = 12;
        }
    }

    let date = new Date(year, month, day);

    year = date.getFullYear();
    month = date.getMonth();
    day = date.getDate();
    console.log(`${year}-${month}-${day}`);
}

solve(2016, 9, 30);
solve(2016, 10, 1);


/* Kude e greshkata v tova reshenie 66/100

function solve(year, month, day) {

    let date = new Date(year, month, day);
    date.setDate(date.getDate() - 1);
    year = date.getFullYear();
    month = date.getMonth();
    day = date.getDate();
    console.log(`${year}-${month}-${day}`);
}
*/