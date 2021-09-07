let titles = document.getElementsByClassName('title');
console.log(Array.isArray(titles));
for (let title of titles) {
    console.log(title);
}