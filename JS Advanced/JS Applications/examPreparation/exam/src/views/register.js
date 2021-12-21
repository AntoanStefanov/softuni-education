import { html } from '../lib.js';
import { register } from '../api/data.js';

const registerTemplate = (onSubmit) =>
  html`<section id="registerPage">
    <form @submit=${onSubmit}>
      <fieldset>
        <legend>Register</legend>

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

        <label for="conf-pass" class="vhide">Confirm Password:</label>
        <input
          id="conf-pass"
          class="conf-pass"
          name="conf-pass"
          type="password"
          placeholder="Confirm Password"
        />

        <button type="submit" class="register">Register</button>

        <p class="field">
          <span>If you already have profile click <a href="/login">here</a></span>
        </p>
      </fieldset>
    </form>
  </section>`;

export function registerPage(ctx) {
  ctx.render(registerTemplate(onSubmit));

  async function onSubmit(ev) {
    ev.preventDefault();
    const formData = new FormData(ev.target); // ev.target is always the form

    // const username = formData.get('username').trim();
    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    const repeatPass = formData.get('conf-pass').trim();
    // const gender = formData.get('gender'); // tuk ne , tova e radio buton

    ev.target.reset();

    // username == '' || email == '' || password == '' || gender == ''
    if (email == '' || password == '' || repeatPass == '') {
      // username == '' || gender == '' ||
      return alert('All fields are required!');
    }

    if (password != repeatPass) {
      return alert("Passwords don't match!");
    }

    // ako tuk hvurli greshka se pokazva alert v request function i koda nadolu ne se izpulnqva
    // (username, email, password, gender)
    await register(email, password);
    // ako vsichko e nared shte produlji koda na dolu
    ctx.updateUserNav();
    ctx.page.redirect('/');
  }
}
