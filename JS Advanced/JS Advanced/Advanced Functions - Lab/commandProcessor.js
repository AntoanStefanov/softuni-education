function createProcessor() {
    let state = '';

    return {
        append,
        removeStart,
        removeEnd,
        print
    };

    function append(string) {
        state += string;
    }

    function removeStart(n) {
        // let strInArray = Array.from(closureString);
        // for (let i = 0; i < n; i++) {
        //     strInArray.shift();
        // }
        // closureString = strInArray.join('');
        state = state.slice(n);

    }

    function removeEnd(n) {
        // let strInArray = Array.from(closureString);
        // for (let i = 0; i < n; i++) {
        //     strInArray.pop();
        // }
        // closureString = strInArray.join('');
        state = state.slice(0, -n);
    }

    function print() {
        console.log(state);
    }


}

let firstZeroTest = createProcessor();
firstZeroTest.append('hello');
firstZeroTest.append('again');
firstZeroTest.removeStart(3);
firstZeroTest.removeEnd(4);
firstZeroTest.print();