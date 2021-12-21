// function validate() {
//     let usernamePattern = /^[a-zA-Z0-9]{3,20}$/m;  
//     let emailPattern = /^.*@.*\..*$/m;
//     let passwordPattern = /^[\w]{5,15}$/m;  //
//     let companyFieldPattern = /^[1-9][0-9]{3}$/m;  

//     const usernameField = document.querySelector('#username');
//     const emailField = document.querySelector('#email');
//     const passwordField = document.querySelector('#password');
//     const confirmPasswordField = document.querySelector('#confirm-password');
//     const checkBox = document.querySelector('#company')
//     const companyInfoArea = document.querySelector('#companyInfo');
//     const companyNumberField = document.querySelector('#companyNumber');
//     const submitButton = document.querySelector('#submit');

//     submitButton.addEventListener('click', (event) => {
//         event.preventDefault();
//         let isDataValid = true;
//         let isCompanyNumberValid = false;

//         if (!usernamePattern.exec(usernameField.value)) {
//             usernameField.style = 'border-color: red';
//             isDataValid = false;
//         } else {
//             usernameField.removeAttribute('style');
//         }

//         if (!emailPattern.exec(emailField.value)) {
//             emailField.style = 'border-color: red';
//             isDataValid = false;
//         } else {
//             emailField.removeAttribute('style');
//         }

//         if (!passwordPattern.exec(confirmPasswordField.value) || passwordField.value !== confirmPasswordField.value) {
//             passwordField.style = 'border-color: red';
//             isDataValid = false;
//         } else {
//             passwordField.removeAttribute('style');
//         }

//         if (!passwordPattern.exec(confirmPasswordField.value) || passwordField.value !== confirmPasswordField.value) {
//             confirmPasswordField.style = 'border-color: red';
//             isDataValid = false;
//         } else {
//             confirmPasswordField.removeAttribute('style');
//         }

//         if (!companyFieldPattern.exec(companyNumberField.value) && checkBox.checked ==true) {
//             companyNumberField.style = 'border-color: red';
//             isCompanyNumberValid = false;
//         } else if (companyFieldPattern.exec(companyNumberField.value) && checkBox.checked ==true){
//             companyNumberField.removeAttribute('style');
//             isCompanyNumberValid = true;
//         }

//         if (isDataValid && checkBox.checked ==false){
//             document.querySelector('#valid').style = 'display: block';
//         } else if (isDataValid && checkBox.checked ==true && isCompanyNumberValid){
//             document.querySelector('#valid').style = 'display: block';
//         } else {
//             document.querySelector('#valid').style = 'display: none';
//         }
//     });

//     checkBox.addEventListener('change', (event) => {
//         if (event.target.checked == true){
//             companyInfoArea.style.display = 'block';

//         } else {
//             companyInfoArea.style.display = 'none';
//         }
//     });
// }


function validate() {
    let usernameRegex = /^[A-Za-z0-9]{3,20}$/gm;
    let passwordRegex = /^[\w]{5,15}$/gm; 
    let emailRegex = /.*?@.*?\..*/gm;

    let usernameEl = document.getElementById('username')
    let emailEl = document.getElementById('email')
    let passwordEl = document.getElementById('password')
    let confirmPasswordEl = document.getElementById('confirm-password')
    let companyNumberEl = document.getElementById('companyNumber');


    let validDivEl = document.getElementById('valid');

    let hiddenCopmanyInfo = document.getElementById('companyInfo');
    let isCompanyCheckBox = document.getElementById('company');
    let submitButton = document.getElementById('submit');


    isCompanyCheckBox.addEventListener('change', function () {
        if (isCompanyCheckBox.checked) {
            hiddenCopmanyInfo.style.display = 'block';
        } else {
            hiddenCopmanyInfo.style.display = 'none';

        }
    })

    submitButton.addEventListener('click', function (e) {
        e.preventDefault();
        let validUsername;
        let validEmail;
        let validPassword;
        let validConfirmPassword;
        let validCompanyNumber;

        if (usernameEl.value.match(usernameRegex) === null) {
            validUsername = false;
            usernameEl.style.borderColor = "red";
        } else {
            validUsername = true;
            usernameEl.style.borderColor = "";
        }

        if (emailEl.value.match(emailRegex) === null) {
            validEmail = false;
            emailEl.style.borderColor = "red";

        } else {
            validEmail = true;
            emailEl.style.borderColor = "";
        }

        if (passwordEl.value.match(passwordRegex) === null) {
            validPassword = false;
            passwordEl.style.borderColor = "red";

        } else {
            validPassword = true;
            passwordEl.style.borderColor = "";
        }
        if (confirmPasswordEl.value.match(passwordRegex) === null) {
            validConfirmPassword = false;
            confirmPasswordEl.style.borderColor = "red";

        } else {
            validConfirmPassword = true;
            confirmPasswordEl.style.borderColor = "";
        }

        if (validPassword || validConfirmPassword) { // || NOT &&
            if (passwordEl.value !== confirmPasswordEl.value) {
                passwordEl.style.borderColor = "red";
                confirmPasswordEl.style.borderColor = "red"; 
                passwordEl.style.borderColor = "";
                confirmPasswordEl.style.borderColor = "";
            }
        }

        if (isCompanyCheckBox.checked) {
            if (companyNumberEl.value > 1000 && companyNumberEl.value <= 9999) {
                validCompanyNumber = true;
                companyNumberEl.style.borderColor = "";

            } else {
                validCompanyNumber = false;
                companyNumberEl.style.borderColor = "red";

            }
        }

        if (validUsername && validEmail && validPassword && validConfirmPassword && (validCompanyNumber || validCompanyNumber === undefined) && (passwordEl.value === confirmPasswordEl.value)) {
            validDivEl.style.display = "block";
        } else {
            validDivEl.style.display = "none";

        }
    });
}