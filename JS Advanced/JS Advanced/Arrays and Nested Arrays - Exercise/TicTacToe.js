function solve(turns) {

    function HaswinnerOnRows(dashboard, player) {
        for (let row of dashboard) {
            let hasWinner = row.every(element => element === player);
            if (hasWinner) {
                return true;
            }
        }
    }

    function HasWinnerOnCols(dashboard, player) {
        for (let column = 0; column < dashboard[0].length; column++) {
            let columnElements = [];
            for (let row = 0; row < dashboard.length; row++) {
                columnElements.push(dashboard[row][column]);
            }
            let hasWinner = columnElements.every(element => element === player);
            if (hasWinner) {
                return true;
            }
        }
    }

    function hasWinnerOnDiagonals(dashboard, player) {
        let primalDiagonal = [];
        let secondaryDiagonal = [];
        for (let i = 0; i < dashboard.length; i++) {
            primalDiagonal.push(dashboard[i][i]);
            secondaryDiagonal.push(dashboard[i][dashboard.length - i - 1]);
        }
        let hasWinner = primalDiagonal.every(element => element === player);
        if (hasWinner) {
            return true;
        }
        hasWinner = secondaryDiagonal.every(element => element === player);
        if (hasWinner) {
            return true;
        }
    }

    let dashboard = [
        [false, false, false],
        [false, false, false],
        [false, false, false],

    ]

    let currentPlayer = 'X';

    for (let i = 0; i < turns.length; i++) {

        let turn = turns[i].split(' ')
        let row = +turn[0];
        let col = +turn[1];


        if (dashboard[row][col] !== false) {
            console.log("This place is already taken. Please choose another!");
            continue;
        }

        dashboard[row][col] = currentPlayer;

        
        if (HaswinnerOnRows(dashboard, currentPlayer) || HasWinnerOnCols(dashboard, currentPlayer) || hasWinnerOnDiagonals(dashboard, currentPlayer)) {
            let output = `Player ${currentPlayer} wins!\n`;
            let rows = [];
            for (let row of dashboard) {
                rows.push(`${row.join('\t')}`);
            }
            output += rows.join('\n');
            return output;
        }

        if (currentPlayer === 'X') {
            currentPlayer = 'O';
        } else {
            currentPlayer = 'X';
        }

        let enoughSpace = false;
        for (let row of dashboard) {
            for (let element of row) {
                if (element === false) {
                    enoughSpace = true;
                    break;
                }
            }
            if (enoughSpace) {
                break;
            }
        }
        if (!enoughSpace) {
            let output = `The game ended! Nobody wins :(\n`;
            let rows = [];
            for (let row of dashboard) {
                rows.push(`${row.join('\t')}`);
            }
            output += rows.join('\n');
            return output;

        }
    }

}