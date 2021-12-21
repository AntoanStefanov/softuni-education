function solve(input) {
    let systems = {};

    for (let data of input) {
        let [system, component, subcomponent] = data.split(' | ');

        if (!(system in systems)) {
            systems[system] = {};
        }
        if (!(component in systems[system])) {
            systems[system][component] = [];
        }

        systems[system][component].push(subcomponent);
    }

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

    sortableTwo.sort(comparer)

    function comparer(a, b) {
        if (a[1].length > b[1].length) {
            return -1
        } else if (a[1].length < b[1].length) {
            return 1
        } else {
            if (a[0].toLowerCase() === b[0].toLowerCase()) {
                return 0;
            }

            if (a[0].toLowerCase() > b[0].toLowerCase()) {
                return 1;
            }

            return -1;
            // return a[0].toLowerCase().localeCompare(b[0].toLowerCase());
        }
    }

    sortableTwo.sort(comparerTwo);

    function comparerTwo(a, b) {
        a[1].sort(insideComprer);
        b[1].sort(insideComprer);



        function insideComprer(c, d) {
            return d[1].length - c[1].length;
            // if (c[1].length > d[1].length) {
            //     return -1
            // } else if (c[1].length < d[1].length) {
            //     return 1
            // } /*else {
            //     return c[0].toLowerCase().localeCompare(d[0].toLowerCase());
            // }*/

        }
    }

    for (let data of sortableTwo) {
        console.log(`${data[0]}`);
        for (let component of data[1]) {
            console.log(`|||${component[0]}`);
            for (let subcomponent of component[1]) {
                console.log(`||||||${subcomponent}`);
            }
        }
    }
}


solve(['SULS | Main Site | Home Page',
    'SULS | Main Site | Login Page',
    'SULS | Main Site | Register Page',
    'SULS | Judge Site | Login Page',
    'SULS | Judge Site | Submittion Page',
    'Lambda | CoreA | A23',
    'SULS | Digital Site | Login Page',
    'Lambda | CoreB | B24',
    'Lambda | CoreA | A24',
    'Lambda | CoreA | A25',
    'Lambda | CoreC | C4',
    'Indice | Session | Default Storage',
    'Indice | Session | Default Security']);