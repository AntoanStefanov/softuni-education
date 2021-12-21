let systems = {
    Indice: {
        Session: ['Default Security', 'Default Storage']
    },
    Lambda: {
        CoreC: ['C4'],
        CoreA: ['A25', 'A23', 'A24'],
        CoreB: ['B24'],
    },
    SULS: {
        'Judge Site': ['Login Page', 'Submission Page'],
        'Digital Site': ['Login Page'],
        'Main Site': ['Register Page', 'Home Page', 'Login Page']
    }
};

// systems = {
//     system: {
//         component: ['subcomponents']
//     }
// };
// [
//     [Indice, {Session: ['Default Security', 'Default Storage']}],
//     [Lambda, [CoreA, ['A25', 'A23', 'A24'], CoreC, ['C4'], CoreB, ['B24']]],
// ]
let sortable = [];
for (let system in systems) {
    sortable.push([system, systems[system]])


}
let sortableTwo = [];
for (let data of sortable) {
    let system = [];
    for (let component in data[1]) {
        system.push([component, data[1][component]]);
    }
    sortableTwo.push([data[0], system]);
}

for (let data of sortableTwo) {
    console.log(data[0]);
    for (let component of data[1]) {
        console.log(`|||${component[0]}`);
        for (let subcomponent of component[1]) {
            console.log(`||||||${subcomponent}`);
        }
    }

}
sortableTwo.sort(comparer)


function comparer(a, b) {
    console.log(a[1].length, b[1].length);
    if (a[1].length > b[1].length) {
        return -1
    } else if (a[1].length < b[1].length) {
        return 1
    } else {
        return a[0].toLowerCase().localeCompare(b[0].toLowerCase());
    }
}





console.log('\n');
for (let data of sortableTwo) {
    console.log(data[0]);
    for (let component of data[1]) {
        console.log(`|||${component[0]}`);
        for (let subcomponent of component[1]) {
            console.log(`||||||${subcomponent}`);
        }
    }
}

sortableTwo.sort(comparerTwo);

function comparerTwo(a, b) {
    a[1].sort(insideComprer);
    b[1].sort(insideComprer);

    function insideComprer(c, d) {
        if (c[1].length > d[1].length) {
            return -1
        } else if (c[1].length < d[1].length) {
            return 1
        } else {
            return c[0].toLowerCase().localeCompare(d[0].toLowerCase());
        }
    }
}


console.log('\n');
for (let data of sortableTwo) {
    console.log(data[0]);
    for (let component of data[1]) {
        console.log(`|||${component[0]}`);
        for (let subcomponent of component[1]) {
            console.log(`||||||${subcomponent}`);
        }
    }
}


sortableTwo.sort(comparerThree);

function comparerThree(a, b) {
    a[1].sort(insideComprer);
    b[1].sort(insideComprer);

    function insideComprer(c, d) {
        c[1].sort(mostInnerComprer);
        d[1].sort(mostInnerComprer);


        function mostInnerComprer(e, f) {
            return e.toLowerCase().localeCompare(f.toLowerCase());
        }
    }
}



console.log('\n');
for (let data of sortableTwo) {
    console.log(data[0]);
    for (let component of data[1]) {
        console.log(`|||${component[0]}`);
        for (let subcomponent of component[1]) {
            console.log(`||||||${subcomponent}`);
        }
    }
}


/*
The Systems you’ve stored must be ordered by amount of components,
in descending order, as first criteria,
and by alphabetical order as second criteria.
The Components must be ordered by amount of Subcomponents, in descending order.
*/

/* All of the elements are strings, and can contain any ASCII character.
The string comparison for the alphabetical order is case-insensitive.
 */