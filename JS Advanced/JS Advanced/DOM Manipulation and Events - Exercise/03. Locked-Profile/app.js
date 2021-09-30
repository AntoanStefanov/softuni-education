// function lockedProfile() {
//     let showMoreButtons = document.querySelectorAll('div.profile button');
//     for (let button of showMoreButtons) {
//         button.addEventListener('click', function (e) {
//             let unlockButton = button.parentElement.querySelector('input[value="unlock"]');
//             let allDivs = Array.from(button.parentElement.querySelectorAll('div'));

//             let hiddenFields = allDivs.filter(div => div.id.includes('HiddenFields'))[0];
//             // or
//             // let hiddenFields = allDivs.find(div => div.id.includes('HiddenFields'));

//             if (unlockButton.checked) {
//                 if (hiddenFields.style.display == '') {
//                     hiddenFields.style.display = 'block';
//                     button.textContent = 'Hide it';
//                 } else {
//                     hiddenFields.style.display = '';
//                     button.textContent = 'Show more';
//                 }
//             }
//         })
//     }
// }
// adding listener to each button up .

// with bubbling below. 

function lockedProfile() {
    let main = document.querySelector('#main');
    main.addEventListener('click', function (e) {
        if (e.target.tagName == 'BUTTON') { //  // if (e.target.tagName === 'BUTTON' && profile.classList.contains('profile')) {...}
            let profile = e.target.parentElement
            let unlockedButton = profile.querySelector('input[type="radio"][value="unlock"]');
            if (unlockedButton.checked) {
               
                let button = e.target;
                let allDivs = Array.from(button.parentElement.querySelectorAll('div'));
                let hiddenFields = allDivs.find(div => div.id.includes('HiddenFields'));
                if (button.textContent == 'Show more') {
                    hiddenFields.style.display = 'block';
                    button.textContent = 'Hide it';
                } else {
                    hiddenFields.style.display = '';
                    button.textContent = 'Show more';
                }
            }
        }
    });
}