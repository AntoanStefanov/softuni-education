function PetShop(input) {
    let numberDogs = Number(input[0]);
    let numberOtherAnimals = Number(input[1]);

    let dogsPrice = numberDogs * 2.50;
    let otherAnimals = numberOtherAnimals * 4;
    let totalCost = dogsPrice + otherAnimals;
    console.log(`${totalCost} lv.`);

}


PetShop(["13", "9"])