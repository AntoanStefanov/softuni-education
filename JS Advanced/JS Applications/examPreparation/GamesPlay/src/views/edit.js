import { editPiece, getPieceById } from '../api/data.js';
import { html } from '../lib.js';

const editTemplate = (piece, onSubmit) =>
  html`<section id="edit-page" class="auth">
      <form @submit=${onSubmit}id="edit">
        <div class="container">
          <h1>Edit Game</h1>
          <label for="leg-title">Legendary title:</label>
          <input
            type="text"
            id="title"
            name="title"
            value=""
            .value=${piece.title}
          />

          <label for="category">Category:</label>
          <input
            type="text"
            id="category"
            name="category"
            value=""
            .value=${piece.category}
          />

          <label for="levels">MaxLevel:</label>
          <input
            type="number"
            id="maxLevel"
            name="maxLevel"
            min="1"
            value=""
            .value=${piece.maxLevel}
          />

          <label for="game-img">Image:</label>
          <input
            type="text"
            id="imageUrl"
            name="imageUrl"
            value=""
            .value=${piece.imageUrl}
          />

          <label for="summary">Summary:</label>
          <textarea
            name="summary"
            id="summary"
            .value=${piece.summary}
          ></textarea>
          <input class="btn submit" type="submit" value="Edit Game" />
        </div>
      </form>
    </section>`;

export async function editPage(ctx) {
  const piece = await getPieceById(ctx.params.id);

  // console.log(ctx); tuk v params stoi id-to
  ctx.render(editTemplate(piece, onSubmit));

  async function onSubmit(ev) {
    ev.preventDefault();

    const formData = new FormData(ev.target); // ev.target is always the form on submit

    const title = formData.get('title').trim();
    const category = formData.get('category').trim();
    const maxLevel = formData.get('maxLevel').trim();
    const imageUrl = formData.get('imageUrl').trim();
    const summary = formData.get('summary').trim();

    if (
      title == '' ||
      category == '' ||
      maxLevel == '' ||
      imageUrl == '' ||
      summary == ''
    ) {
      return alert('All fields are required!');
    }

    await editPiece(ctx.params.id, {
      title,
      category,
      maxLevel,
      imageUrl,
      summary,
    });
    // ako nqma error gore redirect, ako ima koda shte spre do tuk.

    ctx.page.redirect('/details/' + ctx.params.id);
  }
}
