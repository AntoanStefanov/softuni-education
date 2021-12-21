function solve(a, b, c) {
    let sum = a.length + b.length + c.length;
    let avrgLength = Math.floor(sum / 3);

    console.log(sum);
    console.log(avrgLength);
}

solve('chocolate', 'ice cream', 'cake');