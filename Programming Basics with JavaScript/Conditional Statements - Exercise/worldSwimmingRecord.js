function solve(input) {
    let recordInSeconds = Number(input[0]);
    let distanceInMeters = Number(input[1]);
    let secondsForMetering = Number(input[2]);

    let IvanSeconds = distanceInMeters * secondsForMetering;

    let delay = (Math.floor(distanceInMeters / 15)) * 12.5;

    let totalTime = IvanSeconds + delay;

    if (totalTime >= recordInSeconds) {
        console.log(`No, he failed! He was ${(totalTime - recordInSeconds).toFixed(2)} seconds slower.`)
    } else {
        console.log(`Yes, he succeeded! The new world record is ${totalTime.toFixed(2)} seconds.`)
    }
}


solve(["10464", "1500", "20"])
solve(["55555.67", "3017", "5.03"])