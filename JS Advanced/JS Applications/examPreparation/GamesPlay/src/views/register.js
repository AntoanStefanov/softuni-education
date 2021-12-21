import { html } from '../lib.js';
import { register } from '../api/data.js';

const registerTemplate = (onSubmit) =>
  html` <section id="register-page" class="content auth">
    <form @submit=${onSubmit} id="register">
      <div class="container">
        <div class="brand-logo"></div>
        <h1>Register</h1>

        <label for="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          placeholder="maria@email.com"
        />

        <label for="pass">Password:</label>
        <input type="password" name="password" id="register-password" />

        <label for="con-pass">Confirm Password:</label>
        <input type="password" name="confirm-password" id="confirm-password" />

        <input class="btn submit" type="submit" value="Register" />

        <p class="field">
          <span
            >If you already have profile click <a href="/login">here</a></span
          >
        </p>
      </div>
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
    const repeatPass = formData.get('confirm-password').trim();
    // const gender = formData.get('gender'); // tuk ne , tova e radio buton

    ev.target.reset();

    // username == '' || email == '' || password == '' || gender == ''
    if (email == '' || password == '' || repeatPass == '') {
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
