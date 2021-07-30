function solve(input) {
    let numberToConvert = Number(input[0]);
    let currentMetric = input[1];
    let metricToBe = input[2];
    let result;

    if (currentMetric === 'mm') {
        if (metricToBe === 'm') {
            result = numberToConvert / 1000;
        } else if (metricToBe === 'cm') {
            result = numberToConvert / 10;
        }
    } else if (currentMetric === 'm') {
        if (metricToBe === 'mm') {
            result = numberToConvert * 1000;
        } else if (metricToBe === 'cm') {
            result = numberToConvert * 100;
        }
    } else if (currentMetric === 'cm') {
        if (metricToBe === 'mm') {
            result = numberToConvert * 10;
        } else if (metricToBe === 'm') {
            result = numberToConvert / 100;
        }
    }
    console.log(result.toFixed(3));
}

solve(['12', 'mm', 'm'])
solve(["150", "m", "cm"])
solve(["45", "cm", "mm"])
solve(["1201.34", "mm", "cm"])

