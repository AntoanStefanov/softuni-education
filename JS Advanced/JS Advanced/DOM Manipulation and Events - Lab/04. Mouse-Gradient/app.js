function attachGradientEvents() {
    let gradientBoxElement = document.getElementById('gradient');
    let resultElement = document.getElementById('result');
    console.log(Math.floor(50/300 * 100));
    gradientBoxElement.addEventListener('mousemove', function(event) {
        console.log(event);
        // console.log(event.offsetX);
        console.log(event.target);

        console.log(event.target.clientWidth);

        let percent = Math.floor((event.offsetX / event.target.clientWidth ) * 100);
        resultElement.textContent = `${percent}%`;
    })
}