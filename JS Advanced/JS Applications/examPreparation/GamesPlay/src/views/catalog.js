import { getAllPiecesForCatalogPage } from '../api/data.js';
import { html } from '../lib.js';

const catalogTemplate = (pieces) =>
  html`
    <section id="catalog-page">
      <h1>All Games</h1>
      ${pieces.length == 0
        ? html`<h3 class="no-articles">No articles yet</h3>`
        : html`${pieces.map(pieceTemplate)}`}
    </section>
  `;

const pieceTemplate = (piece) =>
  html`<div class="allGames">
    <div class="allGames-info">
      <img src=${piece.imageUrl} />
      <h6>${piece.category}</h6>
      <h2>${piece.title}</h2>
      <a href="/details/${piece._id}" class="details-button">Details</a>
    </div>
  </div>`;

export async function catalogPage(ctx) {
  const pieces = await getAllPiecesForCatalogPage();
  ctx.render(catalogTemplate(pieces));
}
