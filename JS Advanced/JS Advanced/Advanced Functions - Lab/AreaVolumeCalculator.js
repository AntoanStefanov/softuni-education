function area() {
    return Math.abs(this.x * this.y);
};

function vol() {
    return Math.abs(this.x * this.y * this.z);
};


function solve(area, vol, input) {
    let objects = JSON.parse(input);
    let output = [];
    for (let obj of objects) {
        // obj.area = area; zakachash funkciqta kum obekta kato method taka che this da sochi kum obekta
        // obj.vol = vol; // tuk kompozirame funkciite, koeto e promqna na obekta a nie ne iskame tova, iskame samo da gi obrabotim
        // let areaRes = obj.area();
        // let volumeRes = obj.vol();
        // OR // 
        let areaRes = area.call(obj); // obj, params
        let volumeRes = vol.apply(obj); // obj, [params] // podavam obj kato text context
        //
        output.push({ area: areaRes, volume: volumeRes });
    }
    return output;
}


solve(area, vol, `[
    {"x":"1","y":"2","z":"10"},
    {"x":"7","y":"7","z":"10"},
    {"x":"5","y":"2","z":"10"}
    ]`);