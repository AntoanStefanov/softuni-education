function solve(string) {
    let regex = /(\w|\s)*\w(?=")|\w+/g;
    let words = string.match(regex);
    upperCaseWords = words.map(x => x.toUpperCase());
    console.log(upperCaseWords.join(', '));
}

solve('Hi, how are you?');
solve('Functions in JS can be nested, i.e. hold other functions');