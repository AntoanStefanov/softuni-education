function solve() {
  let textToModify = document.getElementById('text').value;
  let modifiedText;
  let namingConvention = document.getElementById('naming-convention').value;

  if (namingConvention === 'Camel Case') {
    textToModify = textToModify.toLowerCase();
    textToModify = textToModify.split(' ');
    for (let i = 1; i < textToModify.length; i++) {
      textToModify[i] = textToModify[i].charAt(0).toUpperCase() + textToModify[i].slice(1);

    }
    modifiedText = textToModify.join('');
  } else if (namingConvention === 'Pascal Case') {
    textToModify = textToModify.toLowerCase();
    textToModify = textToModify.split(' ');
    for (let i = 0; i < textToModify.length; i++) {
      textToModify[i] = textToModify[i].charAt(0).toUpperCase() + textToModify[i].slice(1);
    }
    modifiedText = textToModify.join('');
  } else {
    modifiedText = 'Error!';
  }
  document.getElementById('result').innerHTML = modifiedText;
}