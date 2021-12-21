import { getAllPieces } from '../api/data.js';
import { html } from '../lib.js';
import { getUserData } from '../util.js';

const catalogTemplate = (pieces, isLogged) =>
  html`
    <section id="catalogPage">
      <h1>All Albums</h1>
      ${pieces.length == 0
        ? html`<p>No Albums in Catalog!</p>`
        : html`${pieces.map((piece) => pieceTemplate(piece, isLogged))}`}
    </section>
  `;

const pieceTemplate = (piece, isLogged) =>
  html`<div class="card-box">
    <img src=${piece.imgUrl} />
    <div>
      <div class="text-center">
        <p class="name">Name: ${piece.name}</p>
        <p class="artist">Artist: ${piece.artist}</p>
        <p class="genre">Genre: ${piece.genre}</p>
        <p class="price">Price: $${piece.price}</p>
        <p class="date">Release Date: ${piece.releaseDate}</p>
      </div>
      ${isLogged
        ? html` <div class="btn-group">
            <a href="/details/${piece._id}" id="details">Details</a>
          </div>`
        : null}
    </div>
  </div>`;

export async function catalogPage(ctx) {
  const pieces = await getAllPieces();
  const isLogged = Boolean(getUserData());
  ctx.render(catalogTemplate(pieces, isLogged));
}
