import { html } from '../lib.js';
import { login } from '../api/data.js';
import { notify } from '../notify.js';

const loginTemplate = (onSubmit) =>
  html`<section id="login">
    <form @submit=${onSubmit} id="login-form">
      <div class="container">
        <h1>Login</h1>
        <label for="email">Email</label>
        <input id="email" placeholder="Enter Email" name="email" type="text" />
        <label for="password">Password</label>
        <input
          id="password"
          type="password"
          placeholder="Enter Password"
          name="password"
        />
        <input type="submit" class="registerbtn button" value="Login" />
        <div class="container signin">
          <!-- E TUKA HREFA VODI DO REGISTERA -->
          <p>Dont have an account?<a href="/register">Sign up</a>.</p>
        </div>
      </div>
    </form>
  </section>`;

export function loginPage(ctx) {
  ctx.render(loginTemplate(onSubmit));

  async function onSubmit(ev) {
    ev.preventDefault();
    const formData = new FormData(ev.target); // ev.target is always the form

    const email = formData.get('email').trim();
    const password = formData.get('password').trim();

    if (email == '' || password == '') {
      return notify('All fields are required!'); // ZAMENI NOTIFY S ALERT
    }

    // ako tuk hvurli greshka se pokazva alert v request function i koda nadolu ne se izpulnqva
    await login(email, password);
    // ako vsichko e nared shte produlji koda na dolu
    ctx.updateUserNav();
    ctx.page.redirect('/memes');
  }
}
