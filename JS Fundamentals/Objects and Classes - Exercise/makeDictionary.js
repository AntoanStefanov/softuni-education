function solve(input) {
    let dictionary = {};
    let keys = [];
    for (let JSONstring of input) {
        let obj = (JSON.parse(JSONstring));
        for (let [key, value] of Object.entries(obj)) {
            dictionary[key] = value;
            if (!(keys.includes(key))) {
                keys.push(key);
            }

        }
    }
    keys.sort();
    for (let key of keys) {
        console.log(`Term: ${key} => Definition: ${dictionary[key]}`);
    }

}

solve([
    '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
    '{"Coffee":"ASD THIS SHOULD BE UP"}',
    '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
    '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
    '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
    '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}',
    '{"TEST": "a"}'
])