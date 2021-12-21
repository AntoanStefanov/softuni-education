function solve(array) {
    let food = {};

    for (let i = 0; i < array.length; i += 2) {
        food[array[i]] = +array[i + 1];
    }
    console.log(food);
}


solve(['Yoghurt', '48', 'Rise', '138', 'Apple', '52'])