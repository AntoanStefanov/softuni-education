function solve(number, ...args) {
    number = Number(number);
    for (let command of args) {
        switch (command) {
            case 'chop': number /= 2, console.log(number); break;
            case 'dice': number = Math.sqrt(number), console.log(number); break;
            case 'spice': number++, console.log(number); break;
            case 'bake': number *= 3, console.log(number); break;
            case 'fillet': number -= number * 0.20, console.log(number);
        }
    }
}

solve('32', 'chop', 'chop', 'chop', 'chop', 'chop');