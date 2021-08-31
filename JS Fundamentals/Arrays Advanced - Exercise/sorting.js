function solve(arrayInput) {
    let sortedArray = [];
    let array = arrayInput.slice();

    while (true) {
        let maxNum = Number.MIN_VALUE;
        let maxNumIndex;
        let minNum = Number.MAX_VALUE;
        let minNumIndex;
        for (let i = 0; i < array.length; i++) {
            if (array[i] > maxNum) {
                maxNum = array[i];
                maxNumIndex = array.indexOf(maxNum);

            }

        }
        array.splice(maxNumIndex, 1);
        sortedArray.push(maxNum);
        if (array.length === 0) {
            break;
        }

        for (let i = 0; i < array.length; i++) {

            if (array[i] < minNum) {
                minNum = array[i];
                minNumIndex = array.indexOf(minNum);
            }
        }
        array.splice(minNumIndex, 1);
        sortedArray.push(minNum);

        if (array.length === 0) {
            break;
        }
    }

    console.log(sortedArray.join(' '));
}

solve([1, 21, 3, 52, 69, 63, 31, 2, 18]);