import { editPiece, getPieceById } from '../api/data.js';
import { html } from '../lib.js';

// KAK DA IZBERA OPTIONA KOITO IMA KNIGATA?

const editTemplate = (piece, onSubmit) =>
  html`<section id="edit-page" class="edit">
    <form @submit=${onSubmit} id="edit-form" action="#" method="">
      <fieldset>
        <legend>Edit my Book</legend>
        <p class="field">
          <label for="title">Title</label>
          <span class="input">
            <input type="text" name="title" id="title" .value=${piece.title} />
          </span>
        </p>
        <p class="field">
          <label for="description">Description</label>
          <span class="input">
            <textarea
              name="description"
              id="description"
              .value=${piece.description}
            ></textarea>
          </span>
        </p>
        <p class="field">
          <label for="image">Image</label>
          <span class="input">
            <input
              type="text"
              name="imageUrl"
              id="image"
              .value=${piece.imageUrl}
            />
          </span>
        </p>
        <p class="field">
          <label for="type">Type</label>
          <span class="input">
            <select id="type" name="type" .value=${piece.type}>
              <option value="Fiction">Fiction</option>
              <option value="Romance">Romance</option>
              <option value="Mistery">Mistery</option>
              <option value="Classic">Clasic</option>
              <option value="Other">Other</option>
            </select>
          </span>
        </p>
        <input class="button submit" type="submit" value="Save" />
      </fieldset>
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
    const description = formData.get('description').trim();
    const imageUrl = formData.get('imageUrl').trim();
    const type = formData.get('type');

    // TYPE   // no trim aND EMPTY CHECK because it's from select tag

    if (title == '' || description == '' || imageUrl == '') {
      return alert('All fields are required!');
    }

    await editPiece(ctx.params.id, {
      title,
      description,
      imageUrl,
      type,
    });
    // ako nqma error gore redirect, ako ima koda shte spre do tuk.

    ctx.page.redirect('/details/' + ctx.params.id);
  }
}
