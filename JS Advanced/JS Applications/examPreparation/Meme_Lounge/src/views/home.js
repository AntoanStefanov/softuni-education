import { html } from '../lib.js';
import { getUserData } from '../util.js';

const homeTemplate = () =>
  html`<section id="welcome">
    <div id="welcome-container">
      <h1>Welcome To Meme Lounge</h1>
      <img src="/images/welcome-meme.jpg" alt="meme" />
      <h2>Login to see our memes right away!</h2>
      <div id="button-div">
        <!-- E TUKA DVATA HREFA VAJAT EI -->
        <a href="/login" class="button">Login</a>
        <a href="/register" class="button">Register</a>
      </div>
    </div>
  </section>`;

export function homePage(ctx) {
  // redirect if a user is logged
  if (getUserData()) {
    ctx.page.redirect('/memes');
  } else {
    ctx.render(homeTemplate());
  }
}
