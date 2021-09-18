function extract(content) {
    let res = [];
    let element = document.getElementById(content);
    let elText = element.textContent;
    let regexp = /\((?<betweenBrackets>(.*?))\)/g;
    let matches = [...elText.matchAll(regexp)];
    
    for (let match of matches) {
        let textBetweenBrackets = match.groups['betweenBrackets'];
        res.push(textBetweenBrackets);
    }
    return res.join('; ');
}

console.log(extract("content"));