import { getAllMemes } from '../api/data.js';
import { html } from '../lib.js';

const catalogTemplate = (memes) =>
  html`<section id="meme-feed">
    <h1>All Memes</h1>
    <div id="memes">
      <!-- TUK IMA TERNAREN OPERATOR DALI IMA V BAZATA MEMEOVE ILI NE -->
      ${memes.length == 0
        ? html`<p class="no-memes">No memes in database.</p>`
        : memes.map(memeTemplate)}
    </div>
  </section>`;

const memeTemplate = (meme) =>
  html`<div class="meme">
    <div class="card">
      <div class="info">
        <p class="meme-title">${meme.title}</p>
        <img class="meme-image" alt="meme-img" src=${meme.imageUrl} />
      </div>
      <div id="data-buttons">
        <!-- E TUKA GOLQM TRIK S TOZ HREF HVURLQ TA NA DETAILI NA DADEN MEME -->
        <a class="button" href="/details/${meme._id}">Details</a> 
      </div>
    </div>
  </div>`;

export async function catalogPage(ctx) {
  const memes = await getAllMemes();
  ctx.render(catalogTemplate(memes));
}
