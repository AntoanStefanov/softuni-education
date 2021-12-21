import { getSearchedPieces } from '../api/data.js';
import { html } from '../lib.js';
import { getUserData } from '../util.js';

const searchTemplate = (onSearch, pieces, isLogged, isSearchClicked) =>
  html`
    <section id="searchPage">
      <h1>Search by Name</h1>

      <div class="search">
        <input
          id="search-input"
          type="text"
          name="search"
          placeholder="Enter desired albums's name"
        />
        <button @click=${onSearch} class="button-list">Search</button>
      </div>

      <h2>Results:</h2>

      <!--Show after click Search button-->
      ${isSearchClicked
        ? html`<div class="search-result">
            ${pieces.length == 0
              ? html`<p class="no-result">No result.</p>`
              : html`${pieces.map((piece) => pieceTemplate(piece, isLogged))}`}
          </div>`
        : null}
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

export async function searchPage(ctx) {
  const isLogged = Boolean(getUserData());
  let pieces;
  let isSearchClicked = false;
  ctx.render(searchTemplate(onSearch, pieces, isLogged, isSearchClicked));

  async function onSearch() {
    const query = document.querySelector('.search input').value;
    if (query == '') {
      return alert('Search is required!');
    }

    const pieces = await getSearchedPieces(query);
    let isSearchClicked = true;
    ctx.render(searchTemplate(onSearch, pieces, isLogged, isSearchClicked));
  }
}
