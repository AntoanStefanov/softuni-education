function solve(input) {
    let hourExam = Number(input[0]);
    let minutesExam = Number(input[1]);
    let hourArrived = Number(input[2]);
    let minutesArrived = Number(input[3]);
    let typeArriving;


    let secondsExam = (hourExam * 60 * 60) + (minutesExam * 60);
    let secondsArrived = (hourArrived * 60 * 60) + (minutesArrived * 60);

    let difference = secondsArrived - secondsExam;
    let differenceInMinutes = difference / 60;


    if (differenceInMinutes > 0) {
        typeArriving = 'Late';
    } else if (differenceInMinutes < -30) {
        typeArriving = 'Early';
    } else {
        typeArriving = 'On time';
    }


    differenceInMinutes = Math.abs(differenceInMinutes);

    console.log(typeArriving);

    if (differenceInMinutes >= 60) {
        let differenceInHoursR = differenceInMinutes / 60;
        let differenceInHours = Math.floor(differenceInHoursR);
        differenceInMinutes = Math.round((differenceInHoursR - differenceInHours) * 60);

        if (differenceInMinutes < 10) {
            differenceInMinutes = `0${differenceInMinutes}`;
        }

        switch (typeArriving) {
            case 'Late':
                console.log(`${differenceInHours}:${differenceInMinutes} hours after the start`);
                break;
            case 'Early':
                console.log(`${differenceInHours}:${differenceInMinutes} hours before the start`);

        }
    } else {
        switch (typeArriving) {
            case 'Late':
                console.log(`${differenceInMinutes} minutes after the start`);
                break;
            case 'Early':
                console.log(`${differenceInMinutes} minutes before the start`);
                break;
            case 'On time':
                if (differenceInMinutes > 0) {
                    console.log(`${differenceInMinutes} minutes before the start`);
                }
        }
    }

}

solve(["9",
    "30",
    "9",
    "50"])

solve(["9",
    "00",
    "8",
    "30"])

solve(["9",
    "00",
    "10",
    "30"])

solve(["16",
    "00",
    "15",
    "00"])