function solve(worker) {

    if (worker.dizziness) {
        let neededAmount = 0.1 * worker.weight * worker.experience;
        worker.levelOfHydrated += neededAmount;
        worker.dizziness = false;
    }
    return worker;
}

console.log(solve({
    weight: 80,
    experience: 1,
    levelOfHydrated: 0,
    dizziness: true
}));

solve({
    weight: 120,
    experience: 20,
    levelOfHydrated: 200,
    dizziness: true
});

solve({
    weight: 95,
    experience: 3,
    levelOfHydrated: 0,
    dizziness: false
});