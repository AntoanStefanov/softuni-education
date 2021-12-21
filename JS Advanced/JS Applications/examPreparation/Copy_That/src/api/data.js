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
  return api.get('/data/books?sortBy=_createdOn%20desc');
}

export async function getPieceById(id) {
  return api.get('/data/books/' + id);
}

export async function createPiece(piece) {
  return api.post('/data/books', piece);
}

export async function deletePieceById(id) {
  return api.del('/data/books/' + id);
}

export async function editPiece(id, piece) {
  return api.put('/data/books/' + id, piece);
}

export async function getUserPieces(userId) {
  return api.get(
    `/data/books?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`
  );
}
