import { deletePieceById, getPieceById } from '../api/data.js';
import { html } from '../lib.js';
import { getUserData } from '../util.js';

const detailsTemplate = (piece, isOwner, onDelete) =>
  html`
    <section id="detailsPage">
      <div class="wrapper">
        <div class="albumCover">
          <img src=${piece.imgUrl} />
        </div>
        <div class="albumInfo">
          <div class="albumText">
            <h1>Name: ${piece.name}</h1>
            <h3>Artist: ${piece.artist}</h3>
            <h4>Genre: ${piece.genre}</h4>
            <h4>Price: ${piece.price}</h4>
            <h4>Date: ${piece.releaseDate}</h4>
            <p>Description: ${piece.description}</p>
          </div>
          ${isOwner
            ? html`<div class="actionBtn">
                <a href="/edit/${piece._id}" class="edit">Edit</a>
                <a @click=${onDelete} href="javascript:void(0)" class="remove"
                  >Delete</a
                >
              </div>`
            : null}
        </div>
      </div>
    </section>
  `;

export async function detailsPage(ctx) {
  // console.log(ctx);
  // console.log(ctx.params);
  // id-to otide v params , shtoto v app.js imame :id placeholder
  const piece = await getPieceById(ctx.params.id);

  // check if user is owner and should buttons be displayed
  const userData = getUserData();
  const isOwner = userData && piece._ownerId == userData.id;

  ctx.render(detailsTemplate(piece, isOwner, onDelete));

  async function onDelete() {
    const choice = confirm('Are you sure you want to delete this piece?');
    if (choice) {
      await deletePieceById(ctx.params.id);
      // ako nqma greshka i koda NE spre
      ctx.page.redirect('/catalog');
    }
  }
}
