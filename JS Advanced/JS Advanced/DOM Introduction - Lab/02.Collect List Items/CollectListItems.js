function extractText() {

    let liItems = Array.from(document.querySelectorAll('li')); // [...li]
    let text = (liItems.map(li => li.textContent))
    // document.getElementById('result').textContent = text.join('\n');
    // Viktor izpolzva .value , vmesto .textContent
    document.getElementById('result').value = text.join('\n');


}