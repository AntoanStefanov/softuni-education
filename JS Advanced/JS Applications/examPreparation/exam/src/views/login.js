import { html } from '../lib.js';
import { login } from '../api/data.js';

const loginTemplate = (onSubmit) =>
  html`<section id="loginPage">
    <form @submit=${onSubmit}>
      <fieldset>
        <legend>Login</legend>

        <label for="email" class="vhide">Email</label>
        <input
          id="email"
          class="email"
          name="email"
          type="text"
          placeholder="Email"
        />

        <label for="password" class="vhide">Password</label>
        <input
          id="password"
          class="password"
          name="password"
          type="password"
          placeholder="Password"
        />

        <button type="submit" class="login">Login</button>

        <p class="field">
          <span>If you don't have profile click <a href="/register">here</a></span>
        </p>
      </fieldset>
    </form>
  </section>`;

export function loginPage(ctx) {
  ctx.render(loginTemplate(onSubmit));

  async function onSubmit(ev) {
    ev.preventDefault();
    const formData = new FormData(ev.target); // ev.target is always the form

    const email = formData.get('email').trim();
    const password = formData.get('password').trim();

    // MOJE BI RESET NA INPUTA ? ??????????????
    ev.target.reset();

    if (email == '' || password == '') {
      return alert('All fields are required!');
    }

    // ako tuk hvurli greshka se pokazva alert v request function i koda nadolu ne se izpulnqva
    await login(email, password);
    // ako vsichko e nared shte produlji koda na dolu
    ctx.updateUserNav();
    ctx.page.redirect('/');
  }
}
