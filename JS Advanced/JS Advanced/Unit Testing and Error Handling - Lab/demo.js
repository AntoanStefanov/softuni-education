function solve() {
    try {
        throw Error('my error');
    } catch (err) {
        console.log(err);
    }

}

solve();