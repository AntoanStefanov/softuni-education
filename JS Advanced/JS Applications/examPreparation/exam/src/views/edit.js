import { editPiece, getPieceById } from '../api/data.js';
import { html } from '../lib.js';

const editTemplate = (piece, onSubmit) =>
  html`<section class="editPage">
    <form @submit=${onSubmit}>
      <fieldset>
        <legend>Edit Album</legend>

        <div class="container">
          <label for="name" class="vhide">Album name</label>
          <input
            id="name"
            name="name"
            class="name"
            type="text"
            value="In These Silent Days"
            .value=${piece.name}
          />

          <label for="imgUrl" class="vhide">Image Url</label>
          <input
            id="imgUrl"
            name="imgUrl"
            class="imgUrl"
            type="text"
            value="./img/BrandiCarlile.png"
            .value=${piece.imgUrl}
          />

          <label for="price" class="vhide">Price</label>
          <input
            id="price"
            name="price"
            class="price"
            type="text"
            value="12.80"
            .value=${piece.price}
          />

          <label for="releaseDate" class="vhide">Release date</label>
          <input
            id="releaseDate"
            name="releaseDate"
            class="releaseDate"
            type="text"
            value="October 1, 2021"
            .value=${piece.releaseDate}
          />

          <label for="artist" class="vhide">Artist</label>
          <input
            id="artist"
            name="artist"
            class="artist"
            type="text"
            value="Brandi Carlile"
            .value=${piece.artist}
          />

          <label for="genre" class="vhide">Genre</label>
          <input
            id="genre"
            name="genre"
            class="genre"
            type="text"
            value="Low Country Sound Music"
            .value=${piece.genre}
          />

          <label for="description" class="vhide">Description</label>
          <textarea
            name="description"
            class="description"
            rows="10"
            cols="10"
            .value=${piece.description}
          ></textarea>

          <button class="edit-album" type="submit">Edit Album</button>
        </div>
      </fieldset>
    </form>
  </section> `;

export async function editPage(ctx) {
  const piece = await getPieceById(ctx.params.id);

  // console.log(ctx); tuk v params stoi id-to
  ctx.render(editTemplate(piece, onSubmit));

  async function onSubmit(ev) {
    ev.preventDefault();

    const formData = new FormData(ev.target); // ev.target is always the form on submit

    const name = formData.get('name').trim();
    const imgUrl = formData.get('imgUrl').trim();
    const price = formData.get('price').trim();
    const releaseDate = formData.get('releaseDate').trim();
    const artist = formData.get('artist').trim();
    const genre = formData.get('genre').trim();
    const description = formData.get('description').trim();

    ev.target.reset();

    if (
      name == '' ||
      imgUrl == '' ||
      price == '' ||
      releaseDate == '' ||
      artist == '' ||
      genre == '' ||
      description == ''
    ) {
      return alert('All fields are required!');
    }

    await editPiece(ctx.params.id, {
      name,
      imgUrl,
      price,
      releaseDate,
      artist,
      genre,
      description,
    });
    // ako nqma error gore redirect, ako ima koda shte spre do tuk.

    ctx.page.redirect('/details/' + ctx.params.id);
  }
}
