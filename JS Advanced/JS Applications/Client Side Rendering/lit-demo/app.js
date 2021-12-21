// import { html, render } from 'https://unpkg.com/lit-html?module';

const articleTemplate = (data, onSubmit) => html` <article>
  <input type="text" ?disabled=${data.disabled} .value=${data.color} />
  <h3>${data.title}</h3>
  <div class=${data.color}>
    <p>${data.content}</p>
  </div>
  <footer>Author: ${data.author}</footer>
  <div class="comments">
    <form @submit=${onSubmit}>
      <textarea></textarea>
      <button>Submit comment</button>
    </form>
  </div>
</article>`;

async function start() {
  const data = await (await fetch('./data.json')).json();

  const main = document.querySelector('main');
  const result = data.map(articleTemplate);
  render(result, main);
}

start();
