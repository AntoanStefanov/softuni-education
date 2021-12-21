function solve() {
  let hiddenSections = Array.from(document.querySelectorAll('.hidden'));
  let totalDoc = document.querySelector('#quizzie');
  let correctAnswers = 0;
  let correctWords = [
    "onclick",
    "JSON.stringify()",
    "A programming API for HTML and XML documents"
  ]
  totalDoc.addEventListener('click', function (event) {
    if (event.target.tagName === 'P' && event.target.classList.contains('answer-text')) {
      if (correctWords.includes(event.target.textContent)) {
        correctAnswers++;
      }
      event.target.parentElement.parentElement.parentElement.parentElement.style.display = 'none';
      if (hiddenSections.length > 0) {
        let nextSection = hiddenSections.shift();
        nextSection.style.display = 'block';
      } else {
        let h1El = document.querySelector('li.results-inner h1');
        let res;
        if (correctAnswers === 3) {
          res = "You are recognized as top JavaScript fan!";
        } else {
          res = `You have ${correctAnswers} right answers`;
        }
        h1El.textContent = res;
        document.querySelector('#results').style.display = 'block';
      }
    }

  })
}
