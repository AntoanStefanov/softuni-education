function solve(n, k) {
    let sequence = [1];
    n--;
    while (n > 0) {
        n--;
        let lastKelements = sequence.slice(-k);
        let nextNum = 0;
        for (let i = 0; i < lastKelements.length; i++) {
            nextNum += lastKelements[i];
        }
        sequence.push(nextNum);
    }
    return sequence;
}



console.log(solve(6, 3));
console.log(solve(8, 2));