function solve() {
    let table = document.getElementsByTagName('tbody')[0];
    let rows = table.getElementsByTagName('tr');
    const rgb2hex = (rgb) => `#${rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/).slice(1).map(n => parseInt(n, 10).toString(16).padStart(2, '0')).join('')}`
    let letters = '';
    for (let row of rows) {
        let cells = row.cells;
        for (let cell of cells) {

            let textColorRGB = cell.style.color;
            let bckgrndColortextColorRGB = cell.style.backgroundColor;
            let textColorHex = rgb2hex(textColorRGB);
            let bckgrndColortextColorHex = rgb2hex(bckgrndColortextColorRGB);
            if (textColorHex !== bckgrndColortextColorHex) {
                letters += cell.textContent;
            }
        }
    }
    return letters;
}