function solve(input) {
    let budget = Number(input[0]);
    let numberStatics = Number(input[1]);
    let clothPrice = Number(input[2]);
    let decor = budget * 0.10;

    let allClothPrice = numberStatics * clothPrice;

    if (numberStatics > 150) {
        allClothPrice *= 0.90;
    }

    let totalCost = allClothPrice + decor;
    let leftOver = Math.abs(budget - totalCost).toFixed(2)
    if (budget >= totalCost) {
        console.log("Action!");
        console.log(`Wingard starts filming with ${leftOver} leva left.`);
    } else {
        console.log("Not enough money!");
        console.log(`Wingard needs ${leftOver} leva more.`);
    }
}

solve(['20000', '120', '55.5'])