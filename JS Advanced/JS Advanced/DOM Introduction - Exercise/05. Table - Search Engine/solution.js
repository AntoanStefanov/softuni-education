function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let toSearch = document.getElementById('searchField').value;
      // let bodyWithRows = document.getElementsByTagName('tbody')[0];
      // let rows = bodyWithRows.getElementsByTagName('tr');
      // OR //
      let rows = document.querySelectorAll('tbody tr');
      //
      for (let row of rows) {
         row.setAttribute("class", "");
      }

      for (let row of rows) {
         let currentRowText = row.textContent;
         if (currentRowText.includes(toSearch)) {
            row.setAttribute("class", "select")
         }
      }
   }
}