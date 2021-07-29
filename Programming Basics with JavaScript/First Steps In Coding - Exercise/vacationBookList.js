function solve(input) {
    const totalPages = Number(input[0]);
    const readPagesForHour = Number(input[1]);
    const availableDays = Number(input[2]);
    const neededTimeToRead = totalPages / readPagesForHour;
    const hoursPerDay = neededTimeToRead / availableDays;
    console.log(hoursPerDay);
}

solve(['212', '20', '2']);