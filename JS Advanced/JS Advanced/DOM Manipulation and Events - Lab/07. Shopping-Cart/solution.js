function solve() {
   let shoppingCart = document.querySelector('body div.shopping-cart');
   let checkoutButton = document.querySelector('.checkout');
   let textArea = shoppingCart.querySelector('textarea');
   let allButtons = document.querySelectorAll('button');


   let totalPrice = 0;
   let addedProducts = [];

   shoppingCart.addEventListener('click', function (event) {
      let targetElement = event.target;
      let targetTagName = targetElement.tagName;
      // let targetClassName = targetElement.classList[0]; for 17 line after && targetClassName == 'add-product


      if (targetTagName === 'BUTTON' && targetElement.classList.contains('add-product')) {
         let productElement = targetElement.parentElement.parentElement;
         let productText = productElement.querySelector('.product-title').textContent;
         let productPrice = +productElement.querySelector('.product-line-price').textContent;
         totalPrice += productPrice;
         if (!(addedProducts.includes(productText))) {
            addedProducts.push(productText);
         }
         textArea.textContent += `Added ${productText} for ${productPrice.toFixed(2)} to the cart.\n`;
      }

   });

   checkoutButton.addEventListener('click', function (event) {
      let products = addedProducts.join(', ');
      textArea.textContent += `You bought ${products} for ${totalPrice.toFixed(2)}.`;
      for (let button of allButtons) {
         button.disabled = true;
      }
   })
}