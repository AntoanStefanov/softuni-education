function solve(initialSequence, bombInfo) {
    let bombNumber = bombInfo[0];
    let bombPower = bombInfo[1];
    let sum = 0;
    let index = initialSequence.indexOf(bombNumber);

    while (index !== -1) {
        index -= bombPower;
        if (index < 0) {
            index = 0;
        }

        initialSequence.splice(index, bombPower + bombPower + 1);
        index = initialSequence.indexOf(bombNumber);
    }
    
    for (let i = 0; i < initialSequence.length; i++) {
        sum += initialSequence[i];
    }
    console.log(sum);
}

solve([1, 2, 3, 2, 1], // bez tozi test 80/100,  2 otiva na index 0 i se propuska.
    [2, 1])



solve([1, 2, 2, 4, 2, 2, 2, 9],
    [4, 2]);

solve([1, 4, 4, 2, 8, 9, 1],
    [9, 3]);

solve([1, 7, 7, 1, 2, 3],
    [7, 1]);

solve([1, 1, 2, 1, 1, 1, 2, 1, 1, 1],
    [2, 1]);