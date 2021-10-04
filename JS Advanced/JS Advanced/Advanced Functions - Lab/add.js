function solution(a) {
    let closureVar = a; // moje i bez tazi promenliva a direktno a
    // a kato argument e sushtoto kato suzdadena promenliva
    function add(x) {
        return closureVar + x
    }
    return add;
}


let add5 = solution(5);
console.log(add5(2));
console.log(add5(3));