function solve(input) {
    let length = Number(input[0]);
    let width = Number(input[1]);
    let height = Number(input[2]);
    let percentNumber = Number(input[3]);

    let volume = length * width * height;
    let liters = volume * 0.001;
    let percent = percentNumber * 0.01;
    let neededLiters = liters * (1 - percent);
    console.log(neededLiters);

}

solve(['85', '75', '47', '17']);