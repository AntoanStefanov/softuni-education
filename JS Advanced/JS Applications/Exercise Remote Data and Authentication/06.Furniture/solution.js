window.addEventListener('DOMContentLoaded', () => {
  if (document.URL.includes("login.html")) {
    loginPageFuncionality();
  } else if (document.URL.includes('homeLogged.html')) {
    homeLoggedPageFuncionality();
  } else if (document.URL.includes('home.html')) {
    const isUserLogged = false;
    showProducts(isUserLogged);
  }
});

function loginPageFuncionality() {
  const registerForm = document.querySelector('form[action="/register"]');
  const loginForm = document.querySelector('form[action="/login"]');

  registerForm.addEventListener('submit', onRegister);
  loginForm.addEventListener('submit', onLogin);

  function onSuccessfulLoginOrRegister(userInfo) {
    const userData = {
      email: userInfo.email,
      id: userInfo._id,
      token: userInfo.accessToken
    };

    sessionStorage.setItem('userData', JSON.stringify(userData));

    window.location = './homeLogged.html';

  }

  function onRegister(event) {
    event.preventDefault();
    const formData = new FormData(registerForm);

    const email = formData.get('email').trim()
    const password = formData.get('password').trim()
    const rePass = formData.get('rePass').trim()

    registerUser(email, password, rePass)
      .then(onSuccessfulLoginOrRegister)
      .catch(error => alert('Error: ' + error.message));

    registerForm.reset();
  }

  async function registerUser(email, password, rePass) {

    if (password !== rePass) {
      throw new Error("Passwords don't match");
    }

    const URL = 'http://localhost:3030/users/register';

    const body = {
      email,
      password
    };

    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body)
    }

    const response = await fetch(URL, options);

    if (response.ok != true) {
      const error = await response.json();
      throw new Error(error.message);
    }

    const userInfo = await response.json();

    return userInfo;
  }

  function onLogin(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    const email = formData.get('email').trim();
    const password = formData.get('password').trim();

    loginUser(email, password)
      .then(onSuccessfulLoginOrRegister)
      .catch(error => alert('Error: ' + error.message));

    event.target.reset();
  }

  async function loginUser(email, password) {
    const URL = 'http://localhost:3030/users/login';

    const body = {
      email,
      password
    };

    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body)
    }

    const response = await fetch(URL, options);

    if (response.ok != true) {
      const error = await response.json();
      throw new Error(error.message);
    }

    const userInfo = await response.json();

    return userInfo;
  }

}

function homeLoggedPageFuncionality() {
  const userData = JSON.parse(sessionStorage.getItem('userData'));
  const isUserLogged = true;
  const ordersButton = document.querySelector('div.orders button');

  logOutFuncionality();
  createProductFuncionality();
  showProducts(isUserLogged);
  buyFunctionality();

  ordersButton.addEventListener('click', onAllOrdersClick);
  ordersButton.click();

  function logOutFuncionality() {
    const logOutButton = document.getElementById('logoutBtn');

    logOutButton.addEventListener('click', onLogout);

    function onLogout() {
      logOutButton.disabled = true;
      logout()
        .then(() => {
          sessionStorage.clear();
          window.location = './home.html';
        })
        .catch(err => alert(`Failed to log out. Error: ${err.message}`))
        .finally(() => logOutButton.disabled = false);
    }

    async function logout() {
      const url = 'http://localhost:3030/users/logout';

      const options = {
        method: 'get',
        headers: {
          'X-Authorization': `${userData.token}`
        }
      };

      const response = await fetch(url, options);

      if (response.status !== 204) {
        const err = await response.json();
        throw new Error(err.message);
      }
    }
  }

  function createProductFuncionality() {
    const createProductForm = document.querySelector('.col-md-12 form');
    const createButton = createProductForm.querySelector('button');

    createProductForm.addEventListener('submit', onCreate);

    function onCreate(event) {
      event.preventDefault();
      createButton.textContent = 'Creating...';
      createButton.disabled = true;

      const formData = new FormData(createProductForm);

      const productData = {
        name: formData.get('name'),
        price: formData.get('price'),
        factor: formData.get('factor'),
        img: formData.get('img')
      };

      createProduct(productData)
        .then(() => showProducts(isUserLogged))
        .catch(err => alert('Error: ' + err.message))
        .finally(() => {
          createButton.disabled = false;
          createButton.textContent = 'Create';
        });

      createProductForm.reset();

      async function createProduct(productData) {
        const inputs = Object.values(productData)

        if (inputs.some(input => input === '')) {
          throw new Error('Fill empty input/s');
        }

        const URL = 'http://localhost:3030/data/furniture';

        const options = {
          method: 'post',
          headers: {
            'Content-Type': 'application/json',
            'X-Authorization': `${userData.token}`
          },
          body: JSON.stringify(productData)
        };

        const response = await fetch(URL, options);

        if (response.status !== 200) {
          const err = await response.json();
          throw new Error(err.message);
        }
        const result = await response.json();

        return result;
      }
    }
  }

  function buyFunctionality() {
    const buyButton = document.querySelector('#exercise > div > div > div > div > button');
    buyButton.addEventListener('click', onBuy);

    function onBuy() {
      buyButton.disabled = true;
      buyButton.textContent = 'Buying...';

      const marks = Array.from(document.querySelectorAll('input.mark'));
      const ordersToBeMade = marks.reduce((orders, mark) => {

        if (mark.checked) {
          const productInfo = mark.parentElement.parentElement;

          const productName = productInfo.querySelector('td:nth-child(2)').textContent;
          const productPrice = +productInfo.querySelector('td:nth-child(3)').textContent;

          orders.push(makeEachOrder({
            productName: productName,
            productPrice: productPrice
          }));
        }
        return orders;
      }, []);

      if (ordersToBeMade.length === 0) {
        alert('No product/s chosen!');
        buyButton.disabled = false;
        buyButton.textContent = 'Buy';
        return;
      }

      Promise.all(ordersToBeMade)
        .then(() => {
          alert('You bought the products/s!');
          ordersButton.click();
        })
        .catch(err => alert('Error: ' + err.message))
        .finally(() => {
          marks.forEach(mark => mark.checked = false);
          buyButton.disabled = false;
          buyButton.textContent = 'Buy';
        });
    }

    async function makeEachOrder(productData) {
      const URL = 'http://localhost:3030/data/orders';

      const options = {
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
          'X-Authorization': `${userData.token}`
        },
        body: JSON.stringify(productData)
      };

      const response = await fetch(URL, options);

      if (response.status !== 200) {
        const err = await response.json();
        throw new Error(err.message);
      }
      const result = await response.json();

      return result;
    }
  }

  function onAllOrdersClick() {
    const URL = 'http://localhost:3030/data/orders?where=_ownerId%3D' + `"${userData.id}"`;

    ordersButton.disabled = true;
    ordersButton.textContent = 'Loading...';

    getUserOrders(URL)
      .then(showProductsNamesAndPrices)
      .catch(error => alert('Error: ' + error.message))
      .finally(() => {
        ordersButton.disabled = false;
        ordersButton.textContent = 'All orders';
      });


    function showProductsNamesAndPrices(userMadeOrders) {
      const [productsSpan, priceSpan] = document.querySelectorAll('div.orders span');

      productsNames = [];
      totalPrice = 0;

      userMadeOrders.forEach(productInfo => {
        productsNames.push(productInfo.productName);
        totalPrice += productInfo.productPrice;
      });

      let productsMessage;
      if (productsNames.length === 0) {
        productsMessage = 'No products bought.';
      } else {
        productsMessage = productsNames.join(', ');
      }

      productsSpan.textContent = productsMessage;
      priceSpan.textContent = `${totalPrice.toFixed(2)} $`;
    }

    async function getUserOrders(url) {
      const response = await fetch(url);
      const orders = await response.json();

      return orders;
    }
  }
}

function showProducts(isUserLogged) {
  const table = document.querySelector('.col-md-12 tbody');
  table.replaceChildren(newEl('p', {}, 'Loading...'));

  getProducts()
    .then(products => {
      if (products.length === 0) {
        let message;
        if (isUserLogged) {
          message = 'Be the first to add a new product!';
        } else {
          message = 'Login/Register and be the first to add a new product!';
        }
        table.replaceChildren(newEl('p', {}, message));
        return;
      }
      let productRows = [];
      products.forEach(({ name, price, factor, img }) => {
        const imgEl = newEl('img', { src: img });
        const markEl = newEl('input', { type: 'checkbox', class: 'mark' });

        if (!isUserLogged) {
          markEl.disabled = true;
        }

        const productRow =
          newEl('tr', {},
            newEl('td', {}, imgEl),
            newEl('td', {}, newEl('p', {}, name)),
            newEl('td', {}, newEl('p', {}, price)),
            newEl('td', {}, newEl('p', {}, factor)),
            newEl('td', {}, markEl)
          );
        productRows.push(productRow);
      });
      table.replaceChildren(...productRows);
    })
    .catch(error => {
      const message = 'Error: ' + error.message;
      table.replaceChildren(newEl('p', {}, message));
    });

  async function getProducts() {
    const productsURL = 'http://localhost:3030/data/furniture';

    const response = await fetch(productsURL);
    const products = await response.json();

    return products;
  }
}

function newEl(type, attr, ...content) {
  const element = document.createElement(type);

  for (const prop in attr) {
    if (prop === 'class') {
      let classes = attr[prop].split(' ');
      for (let cls of classes) {
        element.classList.add(cls);
      }
    } else {
      element.setAttribute(prop, attr[prop]);
    }
  }

  for (let item of content) {
    if (typeof item === 'string' || typeof item === 'number') {
      item = document.createTextNode(item);
    }

    element.appendChild(item);
  }

  return element;
}
