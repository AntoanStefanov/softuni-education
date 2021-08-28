function solve(charOne, charTwo) {
    let range = [];
    let charOneCode = charOne.charCodeAt(0);
    let charTwoCode = charTwo.charCodeAt(0);
    let codeToStart = charOneCode;
    let codeToEnd = charTwoCode;
    if (charTwoCode < codeToStart) {
        codeToStart = charTwoCode;
        codeToEnd = charOneCode;
    }

    for (let code = codeToStart + 1; code < codeToEnd; code++) {
        range.push(String.fromCharCode(code));
    }

    console.log(range.join(' '));
}

solve('a', 'd')
solve('C', '#')