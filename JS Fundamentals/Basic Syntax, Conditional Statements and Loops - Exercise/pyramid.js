function solve(n, increment) {
    let stone = 0;
    let marble = 0;
    let lapis = 0;
    let gold = 0;
    let height = 0;
    let totalSquares;
    let outerSquares;
    let innerSquares;

    for (let row = n; row >= 1; row -= 2) {

        height += 1;
        totalSquares = row * row;
        outerSquares = (row - 1) * 4;
        innerSquares = totalSquares - outerSquares;
        if (row == 2 || row == 1) {
            gold += row * row;
            break
        }
        stone += innerSquares;
        if (height % 5 === 0) {
            lapis += outerSquares;
        } else {
            marble += outerSquares;
        }
    }

    console.log(`Stone required: ${Math.ceil(stone * increment)}`);
    console.log(`Marble required: ${Math.ceil(marble * increment)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapis * increment)}`);
    console.log(`Gold required: ${Math.ceil(gold * increment)}`);
    console.log(`Final pyramid height: ${Math.floor(height * increment)}`);
}

solve(11, 1);
solve(11, 0.75);
solve(12, 1);
solve(23, 0.5);
