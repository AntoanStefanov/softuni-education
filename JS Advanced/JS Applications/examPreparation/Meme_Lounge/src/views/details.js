import { deleteMemeById, getMemeById } from '../api/data.js';
import { html } from '../lib.js';
import { getUserData } from '../util.js';

const detailsTemplate = (meme, isOwner, onDelete) =>
  html`<section id="meme-details">
    <h1>Meme Title: ${meme.title}</h1>
    <div class="meme-details">
      <div class="meme-img">
        <img alt="meme-alt" src=${meme.imageUrl} />
      </div>
      <div class="meme-description">
        <h2>Meme Description</h2>
        <p>${meme.description}</p>

        <!-- Buttons Edit/Delete should be displayed only for creator of this meme  -->
        ${isOwner
          ? html`<a class="button warning" href="/edit/${meme._id}">Edit</a>
              <button @click=${onDelete} class="button danger">Delete</button>`
          : null}
      </div>
    </div>
  </section>`;

export async function detailsPage(ctx) {
  // console.log(ctx);
  // console.log(ctx.params);
  // id-to otide v params , shtoto v app.js imame :id placeholder
  const meme = await getMemeById(ctx.params.id);

  // check if user is owner and should buttons be displayed
  const userData = getUserData();
  const isOwner = userData && meme._ownerId == userData.id;

  ctx.render(detailsTemplate(meme, isOwner, onDelete));

  async function onDelete() {
    const choice = confirm('Are you sure you want to delete this meme?');
    if (choice) {
      await deleteMemeById(ctx.params.id);
      // ako nqma greshka i koda NE spre
      ctx.page.redirect('/memes');
    }
  }
}
