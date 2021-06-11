function projectCreation(input) {
    let name = input[0];
    let numberProjects = Number(input[1]);

    console.log(`The architect ${name} will need ${numberProjects * 3} hours to complete ${numberProjects} project/s.`)
}

projectCreation(["George", "4"])
