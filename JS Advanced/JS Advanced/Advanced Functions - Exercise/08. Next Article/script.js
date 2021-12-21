function getArticleGenerator(articles) {
    let divElement = document.querySelector('#content');
    function nextArticle() {
        if (articles.length > 0) {
            let art = document.createElement('article');
            art.textContent = articles.shift();
            divElement.appendChild(art);
        }
    }

    return nextArticle;
}
