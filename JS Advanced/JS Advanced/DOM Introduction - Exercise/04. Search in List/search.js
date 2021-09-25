function search() {
   let listOfTowns = document.getElementById('towns');
   let towns = listOfTowns.getElementsByTagName('li');
   let textSearch = document.getElementById('searchText').value;

   for (let townLiElement of towns) {
      townLiElement.style.fontWeight = 'normal';
      townLiElement.style.textDecoration = 'none';
   }

   let matches = 0;
   for (let townLiElement of towns) {
      if (townLiElement.textContent.includes(textSearch)) {
         matches++;
         townLiElement.style.fontWeight = 'bold';
         townLiElement.style.textDecoration = 'underline';
         townLiElement.style.textDecorationThickness = '1px';

      }
   }
   let result = document.getElementById('result');
   result.textContent = `${matches} matches found`;


}