function extensibleObject() {
    return {
        __proto__: {},
        extend: function (template) {
            for (let prop in template) {
                if (typeof template[prop] == 'function') {
                    this.__proto__[prop] = template[prop];
                } else {
                    this[prop] = template[prop];
                }
            }

        }
    }
}


const myObj = extensibleObject();

// res

// myObj: {
//     __proto__: { }
//     extend: function () {… }
// }



const template = {
    extensionMethod: function () { },
    extensionProperty: 'someString'
}
myObj.extend(template);
let x = 5;
// myObj: {
//     __proto__: {
//         extensionMethod: function () { }
//     },
//     extend: function () { },
//     extensionProperty: 'someString'
// }



