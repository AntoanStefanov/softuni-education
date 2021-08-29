function solve(number) {
    let bar = `${number}% [`;

    for (let i = 1; i <= 10; i++) {
        if (i <= (number / 10)) {
            bar += '%';
        } else {
            bar += '.';
        }
    }
    bar += ']';

    if (number === 100) {
        console.log('100% Complete!');
        console.log(bar);
    } else {
        console.log(bar);
        console.log("Still loading...");
    }
    
}

solve(30);
solve(50);
solve(100);
