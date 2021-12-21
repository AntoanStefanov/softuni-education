function calculator() {
    let firstNumElement;
    let secondNumElement;
    let resultElement;

    return {
        init,
        add,
        subtract,
    }

    function init(selectorOne, selectorTwo, resultSelector) {
        firstNumElement = document.querySelector(selectorOne);
        secondNumElement = document.querySelector(selectorTwo);
        resultElement = document.querySelector(resultSelector);
    }

    function add() {
        resultElement.value = +firstNumElement.value + +secondNumElement.value;
    }

    function subtract() {
        resultElement.value = +firstNumElement.value - +secondNumElement.value;
    }
}


const calculate = calculator();
calculate.init('#num1', '#num2', '#result');


