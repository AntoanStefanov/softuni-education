function solve(array) {
    array.sort(compare);

    function compare(a, b) {
        if (a.length > b.length) {
            return 1;
        } else if (a.length < b.length) {
            return -1;
        } else {
            if (a > b) {
                return 1;
            } else if (b > a) {
                return -1;
            } else {
                return 0;
            }

            // OR -> return a.localeCompare(b); == 10 - 16 lines;
        }
    }

    console.log(array.join('\n'));
}

console.log(['Isacc',
    'Theodor',
    'Jack',
    'Harrison',
    'George']

)