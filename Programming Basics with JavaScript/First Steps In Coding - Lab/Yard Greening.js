function yardGreening(input) {
    let squareMeters = Number(input[0]);
    let greeningPrice = squareMeters * 7.61;
    let discount = greeningPrice * 0.18
    let finalPrice = greeningPrice - discount;

    console.log(`The final price is: ${finalPrice} lv.`)
    console.log(`The discount is: ${discount} lv.`)

}


yardGreening(["550"])