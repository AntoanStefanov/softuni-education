function add(a) {
    let sum = 0;
    sum += a;
    function innerAdd(b) {
        sum += b;
        return innerAdd;
    }
    innerAdd.toString = () => sum;
    // innerAdd.toString = function () { return sum };
    return innerAdd;
}

console.log(add(1)(6)(-3).toString());
