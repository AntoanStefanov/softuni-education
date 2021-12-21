import { getAllPieces } from '../api/data.js';
import { html } from '../lib.js';

const catalogTemplate = (pieces) =>
  html`<section id="dashboard-page" class="dashboard">
    <h1>Dashboard</h1>
    ${pieces.length == 0
      ? html`<p class="no-books">No books in database!</p>`
      : html`<ul class="other-books-list">
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

export async function catalogPage(ctx) {
  const pieces = await getAllPieces();
  ctx.render(catalogTemplate(pieces));
}
