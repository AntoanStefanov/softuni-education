function solve(car) {
    let modifiedCar = {};
    modifiedCar.model = car.model;

    let engines = {
        'Small engine': { power: 90, volume: 1800 },
        'Normal engine': { power: 120, volume: 2400 },
        'Monster engine': { power: 200, volume: 3500 },
    }

    let carriages = {
        'hatchback': { type: 'hatchback', color: 'fill' },
        'coupe': { type: 'coupe', color: 'fill' },
    }

    if (car.power <= 90) {
        modifiedCar.engine = {
            power: engines['Small engine'].power,
            volume: engines['Small engine'].volume,
        }
    } else if (car.power <= 120) {
        modifiedCar.engine = {
            power: engines['Normal engine'].power,
            volume: engines['Normal engine'].volume,
        }
    } else {
        modifiedCar.engine = {
            power: engines['Monster engine'].power,
            volume: engines['Monster engine'].volume,
        }
    }

    modifiedCar.carriage = carriages[car.carriage];
    modifiedCar.carriage.color = car.color;

    if (car.wheelsize % 2 === 0) {
        car.wheelsize--;
    }

    modifiedCar.wheels = [car.wheelsize, car.wheelsize, car.wheelsize, car.wheelsize];

    return modifiedCar;

}


console.log(solve({
    model: 'VW Golf II',
    power: 90,
    color: 'blue',
    carriage: 'hatchback',
    wheelsize: 14
}));

console.log(solve({
    model: 'Opel Vectra',
    power: 110,
    color: 'grey',
    carriage: 'coupe',
    wheelsize: 17
}));