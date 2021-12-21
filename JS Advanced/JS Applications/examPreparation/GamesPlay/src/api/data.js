import * as api from './api.js';

export const login = api.login;
export const register = api.register;
export const logout = api.logout;

// Example
// export async function getAllMovies() {
//     return api.get('/data/movies');
// }

// EXAMPLE
export async function getAllPiecesForHomePage() {
  return api.get('/data/games?sortBy=_createdOn%20desc&distinct=category');
}

export async function getAllPiecesForCatalogPage() {
  return api.get('/data/games?sortBy=_createdOn%20desc');
}

export async function getPieceById(id) {
  return api.get('/data/games/' + id);
}

export async function createPiece(piece) {
  return api.post('/data/games', piece);
}

export async function deletePieceById(id) {
  return api.del('/data/games/' + id);
}

export async function editPiece(id, piece) {
  return api.put('/data/games/' + id, piece);
}

// export async function getUserPieces(userId) {
//   return api.get(
//     `/data/books?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`
//   );
// }

export async function getPieceComments(gameId) {
  return api.get(`/data/comments?where=gameId%3D%22${gameId}%22`);
}

export async function createComment(comment) {
  return api.post('/data/comments', comment);
}
