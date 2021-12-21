function solve(arr) {
    function carFactory() {
        let cars = {};
        return {
            create,
            setProp,
            print,
            inherit
        }

        function inherit(newCar, carToInherit) {
            cars[newCar] = Object.create(cars[carToInherit]);

        }

        function create(carName) {
            cars[carName] = {};
        }

        function setProp(carName, prop, value) {
            if (carName in cars) {
                cars[carName][prop] = value;
            }

        }

        function print(carName) {
            let output = [];
            for (let propName in cars[carName]) {
                output.push(`${propName}:${cars[carName][propName]}`);
            }
            console.log(output.join(','));
        }
    }

    let carConstructor = carFactory();
    for (let data of arr) {
        let info = data.split(' ');
        if (info.includes('inherit')) {
            carConstructor.inherit(info[1], info[3]);
        } else if (info.includes('create')) {
            carConstructor.create(info[1]);
        } else if (info.includes('set')) {
            carConstructor.setProp(info[1], info[2], info[3]);
        } else if (info.includes('print')) {
            carConstructor.print(info[1]);
        }
    }
}


solve(['create c1',
    'set c1 color red',
    'create c2 inherit c1',
    'set c2 model new',
    'print c1',
    'print c2']);

solve(['create pesho',
    'create gosho inherit pesho',
    'create stamat inherit gosho',
    'set pesho rank number1',
    'set gosho nick goshko',
    'print stamat']);
