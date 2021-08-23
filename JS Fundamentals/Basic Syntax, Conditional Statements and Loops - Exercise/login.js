function solve(list) {
    let username = list[0]
    let password = '';
    let timesRemaining = 4;

    for (let i = username.length - 1; i >= 0; i--) {
        password += username[i];
    }

    for (let i = 1; i < list.length; i++) {
        if (list[i] === password) {
            console.log(`User ${username} logged in.`)
        } else {
            timesRemaining--;
            if (timesRemaining === 0) {
                console.log(`User ${username} blocked!`)
                break;
            }
            console.log('Incorrect password. Try again.')
        }
    }
}

solve(['Acer', 'login', 'go', 'let me in', 'recA'])