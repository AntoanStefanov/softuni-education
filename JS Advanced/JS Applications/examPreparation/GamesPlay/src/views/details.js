import {
  createComment,
  deletePieceById,
  getPieceById,
  getPieceComments,
} from '../api/data.js';
import { html } from '../lib.js';
import { getUserData } from '../util.js';

const detailsTemplate = (piece, pieceComments, isOwner, onDelete, onComment) =>
  html`
    <section id="game-details">
      <h1>Game Details</h1>
      <div class="info-section">
        <div class="game-header">
          <img class="game-img" src=${piece.imageUrl} />
          <h1>${piece.title}</h1>
          <span class="levels">MaxLevel: ${piece.maxLevel}</span>
          <p class="type">${piece.category}</p>
        </div>

        <p class="text">${piece.summary}</p>

        <!-- Bonus ( for Guests and Users ) YOU MEAN FOR EVERYBODY -->
        <div class="details-comments">
          <h2>Comments:</h2>
          ${pieceComments == 0
            ? html`<p class="no-comment">No comments.</p>`
            : html`<ul>
                ${pieceComments.map(
                  (piece) => html`<li>Content: ${piece.comment}</li>`
                )}
              </ul>`}
        </div>

        ${isOwner
          ? html`<div class="buttons">
              <a href="/edit/${piece._id}" class="button">Edit</a>
              <a @click=${onDelete} href="javascript:void(0)" class="button"
                >Delete</a
              >
            </div>`
          : null}
      </div>

      <!-- Bonus -->
      <!-- Add Comment ( Only for logged-in users, which is not creators of the current game ) -->
      ${isOwner != null && !isOwner
        ? html`<article class="create-comment">
            <label>Add new comment:</label>
            <!-- why this form doesn't work with enter ? no submit with enter ? why ?'-->
            <form @submit=${onComment} class="form">
              <textarea name="comment" placeholder="Comment......"></textarea>
              <input class="btn submit" type="submit" value="Add Comment" />
            </form>
          </article>`
        : null}
    </section>`;

export async function detailsPage(ctx) {
  // console.log(ctx);
  // console.log(ctx.params);
  // id-to otide v params , shtoto v app.js imame :id placeholder
  const piece = await getPieceById(ctx.params.id);
  const pieceComments = await getPieceComments(ctx.params.id);

  // check if user is owner and should buttons be displayed
  const userData = getUserData();
  const isOwner = userData && piece._ownerId == userData.id;

  ctx.render(
    detailsTemplate(piece, pieceComments, isOwner, onDelete, onComment)
  );

  async function onDelete() {
    const choice = confirm('Are you sure you want to delete this piece?');
    if (choice) {
      await deletePieceById(ctx.params.id);
      // ako nqma greshka i koda NE spre
      ctx.page.redirect('/');
    }
  }

  async function onComment(ev) {
    ev.preventDefault();
    const formData = new FormData(ev.target); // ev.target is always the form on submit

    const comment = formData.get('comment').trim();

    ev.target.reset();

    if (comment == '') {
      return alert('Comment is empty!');
    }

    const gameId = ctx.params.id;
    await createComment({ gameId, comment });
    ctx.page.redirect('/details/' + gameId);
  }
}
