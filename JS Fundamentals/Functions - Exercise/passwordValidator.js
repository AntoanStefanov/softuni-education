function solve(password) {
    let isValid = true;
    let digits = 0;
    let passwordArray = password.split('');

    if (passwordArray.length < 6 || passwordArray.length > 10) {
        console.log("Password must be between 6 and 10 characters");
        isValid = false;
    }

    // 65 - 90 / 97 - 122 / 48 - 57 //

    for (let i = 0; i < passwordArray.length; i++) {
        let charCode = passwordArray[i].charCodeAt(0);
        if (charCode < 48 || (charCode > 57 && charCode < 65) ||
            (charCode > 90 && charCode < 97) || charCode > 122) {
            console.log("Password must consist only of letters and digits");
            isValid = false;
            break;
        }
    }

    for (let i = 0; i < passwordArray.length; i++) {
        let charCode = passwordArray[i].charCodeAt(0);
        if (charCode >= 48 && charCode <= 57) {
            digits++;
            if (digits >= 2) {
                break;
            }
        }
    }

    if (digits < 2) {
        console.log("Password must have at least 2 digits");
        isValid = false;

    }

    if (isValid) {
        console.log('Password is valid');
    }

}

solve('logIn');
solve('MyPass123');
solve('Pa$s$s');