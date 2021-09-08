function solve(x, y, operator) {
    switch (operator) {
        case '+': result = x + y; break;
        case '-': result = x - y; break;
        case '*': result = x * y; break;
        case '/': result = x / y; break;
        case '%': result = x % y; break;
        case '**': result = x ** y; break;
    }
    console.log(result);
}

solve(5, 6, '+');
solve(3, 5.5, '*');