window.addEventListener('load', solution);
// 13:48 - 14:29 

function solution() {
  let fullNameEl = document.getElementById('fname');
  let emailEl = document.getElementById('email');
  let phoneEl = document.getElementById('phone');
  let addressEl = document.getElementById('address');
  let codeEl = document.getElementById('code');

  let inputs = [fullNameEl, emailEl, phoneEl, addressEl, codeEl];

  let listInfoEL = document.getElementById('infoPreview');


  let submitBtn = document.getElementById('submitBTN');
  let editBtn = document.getElementById('editBTN');
  let continueBtn = document.getElementById('continueBTN');

  function newEl(type, attr, ...content) {
    const element = document.createElement(type);

    for (const prop in attr) {
      if (prop === 'class') {
        element.classList.add(attr[prop])
      } else {
        element.setAttribute(prop, attr[prop]);
      }
    }

    for (let item of content) {
      if (typeof item == 'string' || typeof item == 'number') {
        item = document.createTextNode(item);
      }

      element.appendChild(item);
    }

    return element;
  }

  function submitFunc(e) {

    if (fullNameEl.value === '' || emailEl.value === '') {
      return;
    }
    let lis = [
      newEl('li', {}, `Full Name: ${fullNameEl.value}`),
      newEl('li', {}, `Email: ${emailEl.value}`),
      newEl('li', {}, `Phone Number: ${phoneEl.value}`),
      newEl('li', {}, `Address: ${addressEl.value}`),
      newEl('li', {}, `Postal Code: ${codeEl.value}`),
    ];

    for (let li of lis) { // forEach butni tuka posle
      listInfoEL.appendChild(li);
    }

    inputs.forEach(inpt => inpt.value = '');

    submitBtn.disabled = true; // submitBtn.disabled = false;
    editBtn.disabled = false; // submitBtn.disabled = false;
    continueBtn.disabled = false; // submitBtn.disabled = false;


  }

  function editFunc(e) {

    editBtn.disabled = true;
    continueBtn.disabled = true;
    submitBtn.disabled = false;
    let lis = Array.from(listInfoEL.querySelectorAll('li'));
    for (let index = 0; index < lis.length; index++) {
      inputs[index].value = lis[index].textContent.split(': ')[1];
    }
    listInfoEL.innerHTML = '';
  }

  function continueFunction(e) {
    document.getElementById('block').innerHTML = '<h3>Thank you for your reservation!</h3>';

  }

  submitBtn.addEventListener('click', submitFunc);
  editBtn.addEventListener('click', editFunc);
  continueBtn.addEventListener('click', continueFunction);

}
