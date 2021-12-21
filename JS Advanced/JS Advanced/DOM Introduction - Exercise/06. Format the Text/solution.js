function solve() {
  let rawText = document.getElementById('input').value;
  let sentencesArr = rawText.split('.');
  let paragraphsArr = [];
  let paragraph = [];
  let sentenceCount = 0;
  for (let sentence of sentencesArr) {
    if (sentence.length === 0) {
      continue;
    }
    paragraph.push(sentence.trim());
    sentenceCount++;
    if (sentenceCount === 3) {
      paragraph = paragraph.join('.');
      paragraph = `<p>${paragraph}.</p>`;
      paragraphsArr.push(paragraph);
      sentenceCount = 0;
      paragraph = [];
    }
  }
  if (sentenceCount > 0) {
    paragraph = `<p>${paragraph.join('.')}.</p>`;
    paragraphsArr.push(paragraph);
  }
  let formattedText = paragraphsArr.join('');
  document.getElementById('output').innerHTML = formattedText;
}