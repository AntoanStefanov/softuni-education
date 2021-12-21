function createCard(face, suit) {
    let validFaces = ['2', '3', '4', '5', '6', '7', '8', '9',
        '10', 'J', 'Q', 'K', 'A'];
    let validSuits = {
        'S': '\u2660',
        'H': '\u2665',
        'D': '\u2666',
        'C': '\u2663'
    };

    if (!(suit in validSuits) || !(validFaces.includes(face))) {
        throw Error(`Invalid card: ${face + suit}`);
    }

    return {
        face,
        suit: validSuits[suit],
        toString() {
            return `${this.face}${this.suit}`;
        }
    }
}

let x = createCard('A', 'S');
console.log(x.toString())
console.log(createCard('10', 'H'));
console.log(createCard('1', 'C'));
console.log(createCard('2', 'K'));