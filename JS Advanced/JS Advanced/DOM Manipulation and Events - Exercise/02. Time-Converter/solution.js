function attachEventsListeners() {
    let ratios = {
        days: 1,
        hours: 24,
        minutes: 1440,
        seconds: 86400,
    };

    function convert(value, unit) {
        let inDays = value / ratios[unit];
        return {
            days: inDays,
            hours: inDays * ratios.hours,
            minutes: inDays * ratios.minutes,
            seconds: inDays * ratios.seconds
        };
    }

    let main = document.getElementsByTagName('main')[0];


    main.addEventListener('click', function (event) {
        let clickedTarget = event.target;
        if (clickedTarget.tagName === 'INPUT' && clickedTarget.type === 'button') {
            let val = +clickedTarget.previousElementSibling.value;
            let convertFrom = clickedTarget.previousElementSibling.id;
            let res = convert(val, convertFrom);
            for (let unit in res) {
                main.querySelector(`#${unit}`).value = res[unit];
            }
        }

    })
}


function attachEventsListeners() {
    let ratios = {
        days: 1,
        hours: 24,
        minutes: 1440,
        seconds: 86400,
    };

    function convert(value, unit) {
        let inDays = value / ratios[unit];
        return {
            days: inDays,
            hours: inDays * ratios.hours,
            minutes: inDays * ratios.minutes,
            seconds: inDays * ratios.seconds
        };
    }

    let daysInput = document.getElementById('days');
    let hoursInput = document.getElementById('hours');
    let minutesInput = document.getElementById('minutes');
    let secondsInput = document.getElementById('seconds');

    let btns = document.querySelectorAll('input[type="button"]');
    for (let btn of btns) {
        btn.addEventListener('click', onConvert);
    }

    function onConvert(e) {
        let input = e.target.parentElement.querySelector('input[type="text"]');

        let time = convert(+input.value, input.id);
        daysInput.value = time.days;
        hoursInput.value = time.hours;
        minutesInput.value = time.minutes;
        secondsInput.value = time.seconds;

    }


}