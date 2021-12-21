const getToDos = (resourceURL) => {

    return new Promise((resolve, reject) => {

        const request = new XMLHttpRequest();

        request.addEventListener('readystatechange', function () {
            if (request.status === 200 && request.readyState === 4) {
                const data = JSON.parse(request.responseText);
                resolve(data);

            } else if (request.readyState === 4) {
                reject('Error: could not fetch data from server');

            }
        });

        request.open('GET', resourceURL);
        request.send();
    })

};

getToDos('todos/luigi.json')
    .then(data => console.log(data))
    .catch(error => console.log(error));



// promise example
const getSomething = () => {


    return new Promise((resolve, reject) => {
        // here we tipically do the network request, fetch some data
        resolve('some data');
        reject('some error');
    });
}
