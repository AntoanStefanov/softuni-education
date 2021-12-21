function solve(array) {
    let ladyBugs = [];
    let sizeOfField = array[0];
    let ladyBugsIndexes = array[1].split(" ").map(Number);
    let commands = array.slice(2);

    for (let i = 0; i < sizeOfField; i++) {
        if (ladyBugsIndexes.includes(i)) {
            ladyBugs.push(1); // ladybug 
        } else {
            ladyBugs.push(0); // empty house
        }
    }


    for (let index = 0; index < commands.length; index++) {
        let command = commands[index].split(" ");
        let ladyBugIndex = Number(command[0]);
        let direction = command[1];
        let jump = Number(command[2]);
        let successfulLand = false;
        if (ladyBugs[ladyBugIndex] == 0) { // nema pchela na dadeniq index
            continue;
        } else if (ladyBugIndex < 0 || ladyBugIndex >= ladyBugs.length) { // nevaliden index
            continue;
        } else {
            ladyBugs[ladyBugIndex] = 0; // pchelichkata polita
            while (!successfulLand) {
                if (direction == 'right') {
                    ladyBugIndex += jump;
                } else {
                    ladyBugIndex -= jump;
                }
                if (ladyBugIndex < 0 || ladyBugIndex >= ladyBugs.length) {
                    break;
                } else if (ladyBugs[ladyBugIndex] == 0) {
                    ladyBugs[ladyBugIndex] = 1;
                    successfulLand = true;
                }
            }
        }


    }

    console.log(ladyBugs.join(' '));

}

solve([3, '0 1',
    '0 right 1',
    '2 right 1']);

solve([3, '0 1 2',
    '0 right 1',
    '1 right 1',
    '2 right 1']);

solve([5, '3',
    '3 left 2',
    '1 left -2']
)