function solve(array) {
    array.sort((a, b) => a.localeCompare(b));
    let outputArr = [];
    for (let i = 0; i < array.length; i++) {
        outputArr.push(`${i + 1}.${array[i]}`);
    }
    return outputArr.join('\n');
}

console.log(solve(["John", "Bob", "Christina", "Ema"]))