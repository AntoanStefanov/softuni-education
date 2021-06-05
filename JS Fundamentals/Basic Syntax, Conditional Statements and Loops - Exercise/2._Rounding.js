function rounding(number, rNumber) {
    if (rNumber > 15) {
        rNumber = 15
    }
    let num = number.toFixed(rNumber);
    return parseFloat(num);
}