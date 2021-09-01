function solve(array) {
    let concreteForEachDay = [];
    let sum = 0;
    let countNotReadyDays;
    let concreteForDay;
    let numbers = array.map(x => Number(x));


    while (true) {

        for (let i = 0; i < numbers.length; i++) {
            numbers[i]++;
        }
        countNotReadyDays = 0;
        for (i = 0; i < numbers.length; i++) {
            if (numbers[i] <= 30) {
                countNotReadyDays++;
            }
        }

        if (countNotReadyDays === 0) {
            break;
        }

        concreteForDay = countNotReadyDays * 195;
        concreteForEachDay.push(concreteForDay);
        sum += concreteForDay * 1900;
    }
    console.log(concreteForEachDay.join(", "));
    console.log(sum, 'pesos');
}

solve([21, 25, 28]);
solve([29]);
solve([17]);
solve([17, 22, 17, 19, 17]);


