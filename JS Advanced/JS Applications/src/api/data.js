import * as api from './api.js';

export const login = api.login;
export const register = api.register;
export const logout = api.logout;

// Example
// export async function getAllMovies() {
//     return api.get('/data/movies');
// }

// EXAMPLE
export async function getAllMemes() {
  return api.get('/data/memes?sortBy=_createdOn%20desc');
}
