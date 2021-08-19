function solve(input) {
    let searchedBooks = 0;
    let index = 0;
    let searchedBook = input[index];

    while (true) {
        index++;
        let currentBook = input[index];

        if (currentBook === 'No More Books') {
            console.log("The book you search is not here!");
            console.log(`You checked ${searchedBooks} books.`);
            break;
        } else if (currentBook === searchedBook) {
            console.log(`You checked ${searchedBooks} books and found it.`);
            break;
        } else {
            searchedBooks++;
        }
    }
}

solve(["Troy",
    "Stronger",
    "Life Style",
    "Troy"])

solve(["The Spot",
    "Hunger Games",
    "Harry Potter",
    "Torronto",
    "Spotify",
    "No More Books"])