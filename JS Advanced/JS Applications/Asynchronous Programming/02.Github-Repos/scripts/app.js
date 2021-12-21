function loadRepos() {
	let username = document.getElementById('username').value;
	let list = document.getElementById('repos');
	fetch(`https://api.github.com/users/${username}/repos`)
		.then(response => {
			if (response.ok == false) {
				throw new Error(`${response.status} ${response.statusText}`);
			}
			return response.json();
		})
		.then(handleResponse)
		.catch(handleError);

	function handleResponse(repos) {
		list.replaceChildren();
		// vmesto list.innerHTML = '' 
		// innerHTML is bad

		repos.forEach(repo => {
			let aTag = document.createElement('a');
			let item = document.createElement('li');
			aTag.setAttribute('href', repo.html_url);
			aTag.textContent = repo.full_name;
			item.appendChild(aTag);
			list.appendChild(item);
		});
	}

	function handleError(error) {
		list.innerHTML = '';
		list.textContent = `${error.message}`
	}
}