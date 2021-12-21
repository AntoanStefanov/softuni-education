import { html, render } from 'https://unpkg.com/lit-html?module';
import { contacts } from './contacts.js';

const div = document.querySelector('div');

const template = (data) => html` <div class="contact card">
  <div>
    <i class="far fa-user-circle gravatar"></i>
  </div>
  <div class="info">
    <h2>Name: ${data.name}</h2>
    <button
      @click="${(e) => {
        const contactInfoEl = e.target.nextElementSibling;
        if (contactInfoEl.style.display === 'none') {
          contactInfoEl.style.display = 'block';
        } else {
          contactInfoEl.style.display = 'none';
        }
      }}"
      class="detailsBtn"
    >
      Details
    </button>
    <div class="details" id=${data.id}>
      <p>Phone number: ${data.phoneNumber}</p>
      <p>Email: ${data.email}</p>
    </div>
  </div>
</div>`;

render(contacts.map(template), div);
