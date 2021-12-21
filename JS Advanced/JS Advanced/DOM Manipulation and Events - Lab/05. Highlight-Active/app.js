// target is the element that triggered the event (e.g., the user clicked on)
// currentTarget is the element that the event listener is attached to.

function focused() {

    let sectionsDiv = document.querySelector('body div');
    // https://www.youtube.com/watch?v=SqQZ8SttQsI&list=PL4cUxeGkcC9gfoKa5la9dsdCNpuey2s-V&index=10 - bubbling
    sectionsDiv.addEventListener('focusin', function (event) { // focus doesn't bubble

        if (event.target.tagName === 'INPUT') {
            event.target.parentElement.classList.add('focused');
            // event.target.parentElement.className = 'focused';
            console.log('input', event.target); // input
            console.log('div', event.currentTarget); // div

        }
    });
    sectionsDiv.addEventListener('focusout', function (event) { // blurr doesnt bubble.
        event.target.parentElement.classList.remove('focused');
        // event.target.parentElement.className = '';
    });
}
// up doesnt work in judge
// down works
// function focused() {

//     let inputs = document.querySelectorAll('body div div input[type="text"]');
//     for (let input of inputs) {
//         input.addEventListener('focus', function (event) {
//             event.target.parentElement.className = 'focused';

//         });
//         input.addEventListener('blur', function (event) {
//             event.target.parentElement.className = '';

//         });
//     }
// }