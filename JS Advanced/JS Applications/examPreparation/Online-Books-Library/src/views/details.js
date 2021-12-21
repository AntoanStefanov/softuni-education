import {
  deletePieceById,
  getPieceById,
  likePiece,
  totalLikesOnPiece,
  totalLikesOnPieceOnCurrentUser,
} from '../api/data.js';

import { html } from '../lib.js';
import { getUserData } from '../util.js';

const detailsTemplate = (
  piece,
  isOwner,
  onDelete,
  onLike,
  likes,
  currentUserLike
) =>
  html`<section id="details-page" class="details">
    <div class="book-information">
      <h3>${piece.title}</h3>
      <p class="type">Type: ${piece.type}</p>
      <p class="img"><img src=${piece.imageUrl} /></p>
      <div class="actions">
        ${isOwner
          ? html`<a class="button" href="/edit/${piece._id}">Edit</a>
              <a @click=${onDelete} class="button">Delete</a>`
          : null}
        ${isOwner != null && !isOwner && currentUserLike == 0
          ? html`<a class="button" @click=${onLike}>Like</a>`
          : null}

        <div class="likes">
          <img class="hearts" src="/images/heart.png" />
          <span id="total-likes">Likes: ${likes}</span>
        </div>
      </div>
    </div>
    <div class="book-description">
      <h3>Description:</h3>
      <p>${piece.description}</p>
    </div>
  </section>`;

export async function detailsPage(ctx) {
  // console.log(ctx);
  // console.log(ctx.params);
  // id-to otide v params , shtoto v app.js imame :id placeholder
  const userData = getUserData();
  const piece = await getPieceById(ctx.params.id);
  const likes = await totalLikesOnPiece(ctx.params.id);
  let currentUserLike = 0;
  if (userData) {
    currentUserLike = await totalLikesOnPieceOnCurrentUser(
      ctx.params.id,
      userData.id
    );
  }
  // check if user is owner and should buttons be displayed
  const isOwner = userData && piece._ownerId == userData.id;

  ctx.render(
    detailsTemplate(piece, isOwner, onDelete, onLike, likes, currentUserLike)
  );

  async function onDelete() {
    const choice = confirm('Are you sure you want to delete this piece?');
    if (choice) {
      await deletePieceById(ctx.params.id);
      // ako nqma greshka i koda NE spre
      ctx.page.redirect('/catalog');
    }
  }

  async function onLike() {
    const bookId = ctx.params.id; // e tuk promenlivata moje da e commentId, bookId, vij add-vaneto na like kkakvo body chaka
    await likePiece({ bookId }); // tuka vnimavai kakva promenliva se chaka v body-to
    ctx.page.redirect('/details/' + bookId);
  }
}