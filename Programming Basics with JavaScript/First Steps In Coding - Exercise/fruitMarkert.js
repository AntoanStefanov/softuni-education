function solve(input) {
    const strawberryPricePerKG = Number(input[0]);
    const bananasKG = Number(input[1]);
    const orangesKG = Number(input[2]);
    const raspberriesKG = Number(input[3]);
    const strawberryKG = Number(input[4]);

    const raspberriesPricePerKG = strawberryPricePerKG / 2;
    const orangesPricePerKG = raspberriesPricePerKG - (raspberriesPricePerKG * 0.4);
    const bananasPricePerKG = raspberriesPricePerKG - (raspberriesPricePerKG * 0.8);

    const totalRaspberriesPrice = raspberriesKG * raspberriesPricePerKG;
    const totalBananasPrice = bananasKG * bananasPricePerKG;
    const totalOrangesPrice = orangesKG * orangesPricePerKG;
    const totalStrawberriesPrice = strawberryKG * strawberryPricePerKG;
    
    const total = totalRaspberriesPrice + totalBananasPrice + totalOrangesPrice + totalStrawberriesPrice;
    console.log(total);
}

solve(['48', '10', '3.3', '6.5', '1.7'])