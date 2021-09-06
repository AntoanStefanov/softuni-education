function solve(input) {
    let words = {};
    let wordsToSearch = input[0].split(' ');

    for (let i = 0; i < wordsToSearch.length; i++) {
        if (!(wordsToSearch[i] in words)) {
            words[wordsToSearch[i]] = 0;
        } else {
            words[wordsToSearch[i]]++;
        }
    };

    for (let i = 1; i < input.length; i++) {
        let word = input[i];
        if (word in words) {
            words[word]++;
        }
    }

    let wordsSortable = [];

    for (let word in words) {
        wordsSortable.push([word, words[word]]);
    }
    
    wordsSortable.sort((a, b) => b[1] - a[1]);

    for (let arr of wordsSortable) {
        console.log(`${arr[0]} - ${arr[1]}`);
    }
}


solve([
    'this sentence', 'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurances', 'of', 'the'
    , 'words', 'this', 'and', 'sentence', 'sentence', 'sentence', 'because', 'this', 'is', 'your', 'task'
]);