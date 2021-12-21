import { html } from '../lib.js';
import { register } from '../api/data.js';

const registerTemplate = (onSubmit) =>
  html`<section id="register-page" class="register">
    <form @submit=${onSubmit} id="register-form" action="" method="">
      <fieldset>
        <legend>Register Form</legend>
        <p class="field">
          <label for="email">Email</label>
          <span class="input">
            <input type="text" name="email" id="email" placeholder="Email" />
          </span>
        </p>
        <p class="field">
          <label for="password">Password</label>
          <span class="input">
            <input
              type="password"
              name="password"
              id="password"
              placeholder="Password"
            />
          </span>
        </p>
        <p class="field">
          <label for="repeat-pass">Repeat Password</label>
          <span class="input">
            <input
              type="password"
              name="confirm-pass"
              id="repeat-pass"
              placeholder="Repeat Password"
            />
          </span>
        </p>
        <input class="button submit" type="submit" value="Register" />
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
    const repeatPass = formData.get('confirm-pass').trim();
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
    ctx.page.redirect('/catalog');
  }
}
