function loadCommits() {
    let username = document.getElementById('username').value;
    let repo = document.getElementById('repo').value;
    let list = document.getElementById('commits');

    let url = `https://api.github.com/repos/${username}/${repo}/commits`;

    fetch(url)
        .then(response => {
            if (response.ok == false) {
                throw new Error(`Error: ${response.status} (Not Found)`);
            }
            return response.json();
        })
        .then(commits => {
            list.replaceChildren(); // remove all li elements
            commits.forEach(commit => {
                let liEl = document.createElement('li');
                liEl.textContent = `${commit.commit.author.name}: ${commit.commit.message}`;
                list.appendChild(liEl);
            })
        })
        .catch(error => {
            list.replaceChildren(); // remove all li elements
            let liEl = document.createElement('li');
            liEl.textContent = `${error.message}`;
            list.appendChild(liEl);
        });

}