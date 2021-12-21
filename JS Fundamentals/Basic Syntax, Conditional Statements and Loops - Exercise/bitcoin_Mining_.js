function solve(input) {
    let firstDayYouBoughtBitcoin;
    let gold;
    let money = 0;
    let bitcoins = 0;
    for (let i = 0; i < input.length; i++) {
        gold = input[i];
        if ((i + 1) % 3 === 0) {
            gold *= 0.70;
        }
        money += gold * 67.51;
        while (money >= 11949.16) {
            if (bitcoins == 0) {
                firstDayYouBoughtBitcoin = i + 1;
            }
            bitcoins += 1;
            money -= 11949.16;
        };

    }

    console.log(`Bought bitcoins: ${bitcoins}`);
    if (firstDayYouBoughtBitcoin) {
        console.log(`Day of the first purchased bitcoin: ${firstDayYouBoughtBitcoin}`);
    }
    console.log(`Left money: ${money.toFixed(2)} lv.`);

}

solve([100, 200, 300])
solve([50, 100])
solve([3124.15, 504.212, 2511.124])