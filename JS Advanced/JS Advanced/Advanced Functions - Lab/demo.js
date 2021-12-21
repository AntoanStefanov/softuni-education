function contextPrinter(a, b) {
    console.log(this, a, b);
}

function myFunc() {

}

const myObj = {
    name: 'Peter'
};

const otherObj = {
    width: 5,
    height: 3
};
contextPrinter(11, 6);
contextPrinter.apply(myObj, [11, 6]);
// contextPrinter.apply();

contextPrinter.call(otherObj, 11, 6);

// bind pravi kopie na funkciqta i zapazva podadeniq kontekst IZRICHNO.
// fiksira na kude da sochi this .
const boundFunc = contextPrinter.bind(myObj, 4, 5); // bind moje i da se podadat parametri
// boundFunc(2, 3);
boundFunc();

