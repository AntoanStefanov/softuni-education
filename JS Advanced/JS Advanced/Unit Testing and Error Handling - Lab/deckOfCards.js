function printDeckOfCards(cards) {
    let deck = [];
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

    for (let card of cards) {
        let face = card.slice(0, -1);
        let suit = card.slice(-1);
        let currentCard;
        try {
            currentCard = createCard(face, suit);
        } catch (e) {
            console.log(e.message); 
            return;
        }
        deck.push(currentCard.toString());
    }

    console.log(deck.join(' '));
}

printDeckOfCards(['AS', '10D', 'KH', '2C']);
printDeckOfCards(['5S', '3D', 'QD', '1C']);