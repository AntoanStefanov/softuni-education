import { getUserPieces } from '../api/data.js';
import { html } from '../lib.js';
import { getUserData } from '../util.js';

const profileTemplate = (pieces) =>
  html`<section id="my-books-page" class="my-books">
    <h1>My Books</h1>
    ${pieces.length == 0
      ? html`<p class="no-books">No books in database!</p>`
      : html`<ul class="my-books-list">
          ${pieces.map(pieceTemplate)}
        </ul>`}
  </section>`;

const pieceTemplate = (piece) =>
  html`<li class="otherBooks">
    <h3>${piece.title}</h3>
    <p>Type: ${piece.type}</p>
    <p class="img"><img src=${piece.imageUrl} /></p>
    <a class="button" href="/details/${piece._id}">Details</a>
  </li>`;

export async function profilePage(ctx) {
  const userData = getUserData();
  const pieces = await getUserPieces(userData.id);
  ctx.render(profileTemplate(pieces));
}
