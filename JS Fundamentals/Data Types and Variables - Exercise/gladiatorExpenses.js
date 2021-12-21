function solve(lostFightsCount, helmetPrice, swordPrice, shieldPrice, armorPrice,) {
    let brokenHelmets = 0;
    let brokenSwords = 0;
    let brokenShields = 0;
    let brokenArmor = 0;


    for (let i = 1; i <= lostFightsCount; i++) {
        if (i % 2 == 0) {
            brokenHelmets++;
        }
        if (i % 3 == 0) {
            brokenSwords++;
        }

        if (i % 2 == 0 && i % 3 == 0) {
            brokenShields++;
            if (brokenShields % 2 == 0) {
                brokenArmor++;
            }
        }
    }

    console.log(`Gladiator expenses: ${(brokenHelmets * helmetPrice + brokenSwords * swordPrice + brokenShields * shieldPrice + brokenArmor * armorPrice).toFixed(2)} aureus`);
}

solve(7,
    2,
    3,
    4,
    5)

solve(23,
    12.50,
    21.50,
    40,
    200
)