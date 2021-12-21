import * as api from './api.js';

export const login = api.login;
export const register = api.register;
export const logout = api.logout;

// Example
// export async function getAllMovies() {
//     return api.get('/data/movies');
// }

// EXAMPLE
export async function getAllPieces() {
  return api.get('/data/albums?sortBy=_createdOn%20desc&distinct=name');
}

export async function getPieceById(id) {
  return api.get('/data/albums/' + id);
}

export async function createPiece(piece) {
  return api.post('/data/albums', piece);
}

export async function deletePieceById(id) {
  return api.del('/data/albums/' + id);
}

export async function editPiece(id, piece) {
  return api.put('/data/albums/' + id, piece);
}

export async function getSearchedPieces(query) {
  return api.get(`/data/albums?where=name%20LIKE%20%22${query}%22`);
}
