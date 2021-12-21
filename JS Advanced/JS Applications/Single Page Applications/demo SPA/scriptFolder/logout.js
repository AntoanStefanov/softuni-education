import { showHomePage } from "./home.js";

export function onLogout() {
    logout()
        .then(() => {
            sessionStorage.removeItem('userData');
            showHomePage();
        })
        .catch(err => alert(`Failed to log out. ${err.message}`));
}

async function logout() {
    const url = 'http://localhost:3030/users/logout';

    const { token } = JSON.parse(sessionStorage.getItem('userData'));

    await fetch(url, {
        headers: {
            'X-Authorization': `${token}`
        }
    });
}