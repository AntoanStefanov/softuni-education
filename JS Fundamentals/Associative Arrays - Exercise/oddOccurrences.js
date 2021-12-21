function solve(string) {
    let dict = {};
    let words = string.split(' ');
    for (let i = 0; i < words.length; i++) {
        let word = words[i].toLowerCase();
        if (!(word in dict)) {
            dict[word] = 0;
        }
        dict[word]++;
    }

    let sortable = [];

    for (let word in dict) {
        sortable.push([word, dict[word]]);
    }

    let printArr = sortable.filter(arr => arr[1] % 2 !== 0);
    let printWords = [];
    for (let arr of printArr) {
        printWords.push(arr[0]);
    }

    console.log(printWords.join(' '));
}


solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');