function solve(x, y, z) {
    let smallest = x;

    if (y < x && y < z) {
        smallest = y;
    } else if (z < x && z < y){
        smallest = z;
    }

    console.log(smallest);
}

solve(2, 5, 3);