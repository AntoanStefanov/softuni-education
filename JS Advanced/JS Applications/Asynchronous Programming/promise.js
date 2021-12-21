let guestsCount = 101;

let engagementPromise = new Promise(function (resolve, reject) {
    if (guestsCount > 100) {
        reject('Wedding too big');
    } else {
        resolve("Let's get married");
    }

});

engagementPromise
    .then(function (message) {// message e tova vyv resolve funkciqta
        console.log('promise fulfilled');
        console.log(message);
    })
    .catch(function (reasonORerror) { // reason or error e tova koeto e v reject funkciqta
        console.log('promise rejected');
        console.log(reasonORerror);
    })

