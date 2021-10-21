function solve() {
   let authorInputEl = document.getElementById('creator');
   let titleInputEl = document.getElementById('title');
   let categoryInputEl = document.getElementById('category');
   let contentInputEl = document.getElementById('content');

   let createButton = document.getElementsByClassName('btn create')[0];

   let articleSection = document.querySelector('main>section');
   let archiveSection = document.querySelector('aside > section.archive-section > ol');

   function sortArchiveSectionOL(OLorUL) {
      let archiveLIS = Array.from(OLorUL.children);
      function compare(liOne, liTwo) {
         return liOne.textContent.localeCompare(liTwo.textContent);
      }
      archiveLIS.sort(compare);
      OLorUL.innerHTML = '';
      for (let li of archiveLIS) {
         OLorUL.appendChild(li);
      }
   }

   function deleteOrArchiveClick(ev) {
      if (ev.target.classList.contains('delete')) {
         ev.target.parentElement.parentElement.remove();
      } else if (ev.target.classList.contains('archive')) {
         let currentArticle = ev.target.parentElement.parentElement;
         let postTitle = currentArticle.querySelector('h1').textContent;
         let li = document.createElement('li');
         li.textContent = postTitle;
         archiveSection.appendChild(li);
         currentArticle.remove();
         sortArchiveSectionOL(archiveSection);

      }
   }

   function createPost(ev) {
      ev.preventDefault();


      let author = authorInputEl.value;
      let title = titleInputEl.value;
      let category = categoryInputEl.value;
      let content = contentInputEl.value;

      let article = newEl('article', {},
         newEl('h1', {}, title),
         newEl('p', {}, 'Category: ', newEl('strong', {}, category)),
         newEl('p', {}, 'Creator: ', newEl('strong', {}, author)),
         newEl('p', {}, content),
         newEl('div', { class: 'buttons' }, newEl('button', { class: 'btn delete' }, 'Delete'), newEl('button', { class: 'btn archive' }, 'Archive'))
      )
      articleSection.appendChild(article);

      let buttons = article.querySelector('.buttons');
      buttons.addEventListener('click', deleteOrArchiveClick);

      authorInputEl.value = '';
      titleInputEl.value = '';
      categoryInputEl.value = '';
      contentInputEl.value = '';
   }


   function newEl(type, attr, ...content) {
      const element = document.createElement(type);

      for (const prop in attr) {
         if (prop === 'class') {
            let classes = attr[prop].split(' ');
            for (let cls of classes) {
               element.classList.add(cls) // TUK NE MOJE DA SE DOBAVI IME NA KLAS V KOITO IMA SPACE 
            }
         } else {
            element.setAttribute(prop, attr[prop]);
         }
      }

      for (let item of content) {
         if (typeof item == 'string' || typeof item == 'number') {
            item = document.createTextNode(item);
         }

         element.appendChild(item);
      }

      return element;
   }

   createButton.addEventListener('click', createPost);

}
