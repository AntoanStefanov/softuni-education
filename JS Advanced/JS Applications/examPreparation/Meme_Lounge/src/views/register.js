import { html } from '../lib.js';
import { register } from '../api/data.js';
import { notify } from '../notify.js';

const registerTemplate = (onSubmit) =>
  html`<section id="register">
    <form @submit=${onSubmit} id="register-form">
      <div class="container">
        <h1>Register</h1>
        <label for="username">Username</label>
        <input
          id="username"
          type="text"
          placeholder="Enter Username"
          name="username"
        />
        <label for="email">Email</label>
        <input id="email" type="text" placeholder="Enter Email" name="email" />
        <label for="password">Password</label>
        <input
          id="password"
          type="password"
          placeholder="Enter Password"
          name="password"
        />
        <label for="repeatPass">Repeat Password</label>
        <input
          id="repeatPass"
          type="password"
          placeholder="Repeat Password"
          name="repeatPass"
        />
        <div class="gender">
          <input type="radio" name="gender" id="female" value="female" />
          <label for="female">Female</label>
          <input type="radio" name="gender" id="male" value="male" checked />
          <label for="male">Male</label>
        </div>
        <input type="submit" class="registerbtn button" value="Register" />
        <div class="container signin">
          <!-- E TUKA HREFA VODI DO LOGINA -->
          <p>Already have an account?<a href="/login">Sign in</a>.</p>
        </div>
      </div>
    </form>
  </section>`;

export function registerPage(ctx) {
  ctx.render(registerTemplate(onSubmit));

  async function onSubmit(ev) {
    ev.preventDefault();
    const formData = new FormData(ev.target); // ev.target is always the form

    const username = formData.get('username').trim();
    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    const repeatPass = formData.get('repeatPass').trim();
    const gender = formData.get('gender'); // tuk ne , tova e radio buton

    if (username == '' || email == '' || password == '' || gender == '') {
      return notify('All fields are required!'); // ZAMENI NOTIFY S ALERT
    }

    if (password != repeatPass) {
      return notify("Passwords don't match!"); // ZAMENI NOTIFY S ALERT
    }

    // ako tuk hvurli greshka se pokazva alert v request function i koda nadolu ne se izpulnqva
    await register(username, email, password, gender);
    // ako vsichko e nared shte produlji koda na dolu
    ctx.updateUserNav();
    ctx.page.redirect('/memes');
  }
}
