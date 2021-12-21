// making request module
const host = 'http://localhost:3030';

async function request(url, options) {
    try {
        const response = await fetch(host + url, options);

        if (response.ok != true) {
            if (response.status === 403) {
                sessionStorage.removeItem('userData');
            }
            const error = await response.json();
            throw new Error(error.message);
        }

        if (response.status === 204) {
            return response;
        }

        return response.json();

    } catch (err) {
        alert(err.message);
        // throw, за да може този който е извикал фунцията също да разбере че има грешка
        throw err;
    }
}

function createOptions(method = 'GET', data) {
    const options = {
        method,
        headers: {}
    };

    if (data !== undefined) {
        options.headers['Content-Type'] = 'application/json';
        options.body = JSON.stringify(data);
    }

    const userData = JSON.parse(sessionStorage.getItem('userData'));

    if (userData !== null) {
        options.headers['X-Authorization'] = userData.token;
    }

    return options;
}

async function get(url) {
    return request(url, createOptions());
}

async function post(url, data) {
    return request(url, createOptions('POST', data));
}

async function put(url, data) {
    return request(url, createOptions('PUT', data));
}

async function del(url) {
    return request(url, createOptions('DELETE'));
}

async function login(email, password) {
    const response = await request('/users/login', createOptions('POST', { email, password }));

    const userData = {
        email: response.email,
        id: response._id,
        token: response.accessToken
    };

    sessionStorage.setItem('userData', JSON.stringify(userData));
}

async function register(email, password) {
    const response = await request('/users/register', createOptions('POST', { email, password }));

    const userData = {
        email: response.email,
        id: response._id,
        token: response.accessToken
    };

    sessionStorage.setItem('userData', JSON.stringify(userData));
}

async function logout() {
    await request('/users/logout', createOptions());
    sessionStorage.removeItem('userData');
}

export {
    get,
    post,
    put,
    del,
    login,
    register,
    logout
};
