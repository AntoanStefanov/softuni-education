function solve(input) {
    let VIPlist = [];
    let regularList = [];
    let hasPartyStarted = false;
    for (let guest of input) {
        if (guest === 'PARTY') {
            hasPartyStarted = true;
            continue;
        }
        if (!hasPartyStarted) {
            if (guest.match(/^\d/)) {
                VIPlist.push(guest);
            } else {
                regularList.push(guest);
            }
        } else {
            let indexVIP = VIPlist.indexOf(guest);
            let indexRegular = regularList.indexOf(guest);

            if (indexVIP !== -1) {
                VIPlist.splice(indexVIP, 1);
            } else if (indexRegular !== 1) {
                regularList.splice(indexRegular, 1);
            }
        }
    }
    let missedParty = VIPlist.length + regularList.length;

    console.log(missedParty);
    console.log(VIPlist.join('\n'));
    console.log(regularList.join('\n'));

}

solve(['7IK9Yo0h',
    '9NoBUajQ',
    'Ce8vwPmE',
    'SVQXQCbc',
    'tSzE5t0p',
    'PARTY',
    '9NoBUajQ',
    'Ce8vwPmE',
    'SVQXQCbc'
]);