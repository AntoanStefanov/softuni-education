function create(words) {
   let content = document.getElementById('content');
   content.addEventListener('click', reveal);

   for (let word of words) {

      let divElement = document.createElement('div');
      let paragraph = document.createElement('p');
      paragraph.textContent = word;
      paragraph.style.display = 'none';
      divElement.appendChild(paragraph);

      // divElement.addEventListener('click', function (event) {
      //    // event.currentTarget.children[0].style.display = 'block';
      //    let paragraph = divElement.getElementsByTagName('p')[0];
      //    paragraph.style.display = 'block'; 
      // })
      // or
      // divElement.addEventListener('click', reveal);
      //

      content.appendChild(divElement);
   }

   function reveal(e) {
      // console.log(this);
      if (e.target.tagName === 'DIV' && e.target !== content) { // e.target.id !== 'content
         e.target.children[0].style.display = 'block';
      }
   }
}