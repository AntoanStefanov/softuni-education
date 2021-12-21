window.addEventListener('load', solve);

function solve() {

    let genreInputEl = document.getElementById('genre');
    let songNameInputEl = document.getElementById('name');
    let authorInputEl = document.getElementById('author');
    let dateInputEl = document.getElementById('date');

    let addButtonEl = document.getElementById('add-btn');

    let hitsContainerDIV = document.querySelector('#all-hits .all-hits-container');
    let likesElPara = document.querySelector('#total-likes .likes p');

    let savedHitsDIV = document.querySelector('#saved-hits .saved-container');
    
    function onClickCallback(e) {
        e.preventDefault();
        if (genreInputEl.value === '' || songNameInputEl === '' || authorInputEl.value === '' || dateInputEl.value === '') {
            genreInputEl.value = '';
            songNameInputEl.value = '';
            authorInputEl.value = '';
            dateInputEl.value = '';
            return;
        }

        let genre = genreInputEl.value;
        let songName = songNameInputEl.value;
        let author = authorInputEl.value;
        let date = dateInputEl.value;

        let saveBtn = newEl('button', { class: 'save-btn' }, "Save song");
        let likeBtn = newEl('button', { class: 'like-btn' }, "Like song");
        let delBtn = newEl('button', { class: 'delete-btn' }, "Delete");

        let divForInfo = newEl('div', { class: 'hits-info' },
            newEl('img', { src: "./static/img/img.png" }),
            newEl('h2', {}, `Genre: ${genre}`),
            newEl('h2', {}, `Name: ${songName}`),
            newEl('h2', {}, `Author: ${author}`),
            newEl('h3', {}, `Date: ${date}`),
            saveBtn,
            likeBtn,
            delBtn,
        );

        hitsContainerDIV.appendChild(divForInfo);

        genreInputEl.value = '';
        songNameInputEl.value = '';
        authorInputEl.value = '';
        dateInputEl.value = '';



        likeBtn.addEventListener('click', function (e) {
            let text = likesElPara.textContent;
            let currentLikes = Number(text.slice(-1));
            currentLikes++;
            text = text.slice(0, -1) + `${currentLikes}`;
            likesElPara.textContent = text;
            likeBtn.disabled = true;
        });

        saveBtn.addEventListener('click', function (e) {
            let songDIV = e.target.parentElement;
            let SaveBtn = songDIV.querySelector('.save-btn');
            let LikeBtn = songDIV.querySelector('.like-btn');
            SaveBtn.remove();
            LikeBtn.remove();
            savedHitsDIV.appendChild(songDIV);
        });

        delBtn.addEventListener('click', function (e) {
            let songDIV = e.target.parentElement;
            songDIV.remove();
        })

    }


    addButtonEl.addEventListener('click', onClickCallback);


    function newEl(type, attr, ...content) {
        const element = document.createElement(type);

        for (const prop in attr) {
            if (prop === 'class') {
                let classes = attr[prop].split(' ');
                for (let cls of classes) {
                    element.classList.add(cls);
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
}