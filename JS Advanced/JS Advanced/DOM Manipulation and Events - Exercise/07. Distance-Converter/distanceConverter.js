function attachEventsListeners() {
    let ratios = {
        m: 1,
        km: 1000,
        cm: 0.01,
        mm: 0.001,
        mi: 1609.34,
        yrd: 0.9144,
        ft: 0.3048,
        in: 0.0254
    };

    function convert(value, unit) {
        let inM = value / ratios[unit];
        return {
            m: inM,
            km: inM * ratios.km,
            cm: inM * ratios.cm,
            mm: inM * ratios.mm,
            mi: inM * ratios.mi,
            yrd: inM * ratios.yrd,
            ft: inM * ratios.ft,
            in: inM * ratios.in,
        };
    }

    let convertBtn = document.getElementById('convert');
    convertBtn.addEventListener('click', function (event) {
        let val = +document.getElementById('inputDistance').value;
        let convertFrom = document.getElementById('inputUnits').value;
        let convertTo = document.getElementById('outputUnits').value;
        let outputEl = document.getElementById('outputDistance');
        let obj = convert(val, convertTo);
        outputEl.value = obj[convertFrom];
        
    })
}