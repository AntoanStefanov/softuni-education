function solve(array, start, end) {
    let indexStart = array.indexOf(start);
    let indexEnd = array.indexOf(end) + 1;
    return array.slice(indexStart, indexEnd);
}

console.log(solve(['Pumpkin Pie',
    'Key Lime Pie',
    'Cherry Pie',
    'Lemon Meringue Pie',
    'Sugar Cream Pie'],
    'Key Lime Pie',
    'Lemon Meringue Pie'));