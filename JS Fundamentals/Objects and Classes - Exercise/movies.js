function solve(array) {
    let movies = [];

    for (let i = 0; i < array.length; i++) {
        let info = array[i].split(' ');
        let addIndex = info.indexOf('addMovie');
        let directorIndex = info.indexOf('directedBy');
        let dateIndex = info.indexOf('onDate');


        if (addIndex > -1) {
            movies.push({ name: info.slice(addIndex + 1).join(' ') });
        } else if (directorIndex > -1) {
            let movieName = info.slice(0, directorIndex).join(' ');
            let director = info.slice(directorIndex + 1).join(' ');

            // for (movieNumber in movies) {
            //     if (movieName === movies[movieNumber].name) {
            //         movies[movieNumber]['director'] = director;
            //     }
            // }

            movies.forEach(movie => {
                if (movieName === movie.name) {
                    movie.director = director;
                }
            })

        } else if (dateIndex > -1) {
            let movieName = info.slice(0, dateIndex).join(' ');
            let date = info.slice(dateIndex + 1).join(' ');

            for (movieNumber in movies) {
                if (movieName === movies[movieNumber].name) {
                    movies[movieNumber]['date'] = date;
                }
            }
        }
    }
    movies.push({ director: 'Harry Potter' })
    for (let movie of movies) {
        if (['name', 'date', 'director'].every(Object.prototype.hasOwnProperty, movie)) {
            console.log(JSON.stringify(movie));
        };
    }
}

solve([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
]);