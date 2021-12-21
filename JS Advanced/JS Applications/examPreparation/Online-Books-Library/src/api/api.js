import { getUserData, setUserData, clearUserData } from '../util.js';

// making request module
const host = 'http://localhost:3030';

async function request(url, options) {
  try {
    const response = await fetch(host + url, options);

    if (response.ok != true) {
      if (response.status === 403) {
        clearUserData();
      }
      const error = await response.json();
      throw new Error(error.message);
    }

    ///
    try {
      return await response.json();
    } catch (error) {
      return response;
    }
    ///
    // tova zamenq gornoto

    /*
    if (response.status === 204) {
      return response;
    }

    return response.json();
    */
  } catch (err) {
    // ZAMENI NOTIFY S ALERT
    // alert(err.message); OTKOMENTIRAI TOVA ! I MAHNI NOTIFY TOVA E BONUSA
    alert(err.message);
    // throw, за да може този който е извикал фунцията също да разбере че има грешка
    throw err;
  }
}

function createOptions(method = 'GET', data) {
  const options = {
    method,
    headers: {},
  };

  if (data !== undefined) {
    options.headers['Content-Type'] = 'application/json';
    options.body = JSON.stringify(data);
  }

  const userData = getUserData();

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
  const response = await post('/users/login', { email, password });

  // TUK PISHEM KAKVOTO E NUJNO PO ZADACHATA OT USER INFOTO,
  // ime, pol, email, kvot trq vzimame
  const userData = {
    username: response.username,
    email: response.email,
    id: response._id,
    token: response.accessToken,
    // gender: response.gender, // TUK ZARADI AVATARA NA PROFILE-A e NUJEN POLA MEME LOUNGE
  };

  setUserData(userData);
  return response; // za kvo ?
  // shotot nqkoi moje da iska da go izpolzva
}

// kato parameter se priema vsichko nujno za registraciqta, sprqmo zadachata
// (username, email, password, gender)
async function register(email, password) {
  const response = await post('/users/register', {
    // username,
    email,
    password,
    // gender,
  });

  const userData = {
    // username: response.username,
    email: response.email,
    id: response._id,
    token: response.accessToken,
    // gender: response.gender,
  };

  setUserData(userData);
  return response; // za kvo go napisa toz ?
  // shotot nqkoi moje da iska da go izpolzva
}

async function logout() {
  get('/users/logout');
  clearUserData();
}

export { get, post, put, del, login, register, logout };
