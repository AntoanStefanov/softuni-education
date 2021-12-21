import { getAllPiecesForHomePage } from '../api/data.js';
import { html } from '../lib.js';
// import { getUserData } from '../util.js';

const homeTemplate = (pieces) =>
  html`<section id="welcome-world">
    <div class="welcome-message">
      <h2>ALL new games are</h2>
      <h3>Only in GamesPlay</h3>
    </div>
    <img src="./images/four_slider_img01.png" alt="hero" />
    <div id="home-page">
      <h1>Latest Games</h1>
      ${pieces.length == 0
        ? html`<p class="no-articles">No games yet</p>`
        : html`${pieces.map(pieceTemplate)}`}
    </div>
  </section>`;

const pieceTemplate = (piece) =>
  html`<div class="game">
    <div class="image-wrap">
      <img src=${piece.imageUrl} />
    </div>
    <h3>${piece.title}</h3>
    <div class="rating">
      <span>☆</span><span>☆</span><span>☆</span><span>☆</span><span>☆</span>
    </div>
    <div class="data-buttons">
      <a href="/details/${piece._id}" class="btn details-btn">Details</a>
    </div>
  </div>`;

export async function homePage(ctx) {
  const pieces = await getAllPiecesForHomePage();
  ctx.render(homeTemplate(pieces));

  //     // redirect if a user is logged
  //   if (getUserData()) {
  //     ctx.page.redirect('/memes');
  //   } else {
  //     ctx.render(homeTemplate());
  //   }
}
