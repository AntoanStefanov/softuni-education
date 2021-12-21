function solve() {

    let menuTo = document.getElementById('selectMenuTo');
    menuTo.options[0].value = 'binary';
    menuTo.options[0].text = 'Binary';
    let hexadecimalOption = document.createElement('option');
    hexadecimalOption.value = 'hexadecimal';
    hexadecimalOption.text = 'Hexadecimal';
    menuTo.add(hexadecimalOption);
    
    let button = document.getElementsByTagName('button')[0];
    let result = document.getElementById('result');

    button.onclick = function () {
        let number = +document.getElementById('input').value;
        let convertTo = menuTo.value;

        if (convertTo === 'binary') {
            let binary = [];
            while (number > 0) {
                let currentBinary = number % 2;
                binary.push(currentBinary);
                number = Math.floor(number / 2);
            }
            binary.reverse();
            result.value = binary.join('');
        } else if (convertTo === 'hexadecimal') {
            let hexadecimal = [];
            let values = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            while (number > 0) {
                let currentHexadecimal = number % 16;
                if (currentHexadecimal > 9) {
                    currentHexadecimal = values[currentHexadecimal];
                }
                hexadecimal.push(currentHexadecimal);
                number = Math.floor(number / 16);
            }
            hexadecimal.reverse();
            result.value = hexadecimal.join('');
        }
    }

}