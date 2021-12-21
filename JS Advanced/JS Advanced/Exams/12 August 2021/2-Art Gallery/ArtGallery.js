// 18:58 - 19:57:59 ; 59 mins 59 secs. 3 zadachi za 4 chasa
class ArtGallery {
    constructor(creator) {
        this.creator = creator;
        this.possibleArticles = {
            "picture": 200,
            "photo": 50,
            "item": 250
        };
        this.listOfArticles = []; // model, name, quantity
        this.guests = []; // name, points, buys;
    }

    addArticle(articleModel, articleName, quantity) {
        articleModel = articleModel.toLowerCase();
        if (!(articleModel in this.possibleArticles)) {
            throw new Error("This article model is not included in this gallery!");
        }
        let exists = false;
        for (let article of this.listOfArticles) {
            if (article[0] === articleModel && article[1] === articleName) {
                article[2] += quantity;
                exists = true;
                break;
            }
        }
        if (!exists) {
            this.listOfArticles.push([articleModel, articleName, quantity]);
        }

        return `Successfully added article ${articleName} with a new quantity- ${quantity}.`

    }

    inviteGuest(guestName, personality) {
        for (let guest of this.guests) {
            if (guest[0] === guestName) {
                throw new Error(`${guestName} has already been invited.`);
            }
        }

        let points;
        let personalities = {
            'Vip': 500,
            'Middle': 250
        }
        if (!(personality in personalities)) {
            points = 50;
        } else {
            points = personalities[personality];
        }
        this.guests.push([guestName, points, 0]);
        return `You have successfully invited ${guestName}!`;
    }

    buyArticle(articleModel, articleName, guestName) {
        let doesArticleExists = false;
        let foundArticle;
        for (let articleInfo of this.listOfArticles) {
            if (articleInfo[0] === articleModel && articleInfo[1] === articleName) {
                doesArticleExists = true;
                foundArticle = articleInfo;
                break;
            }
        }
        if (doesArticleExists) {
            if (foundArticle[2] > 0) {
                let doesGuestExists = false;
                let foundGuest;
                for (let guest of this.guests) {
                    if (guest[0] == guestName) {
                        doesGuestExists = true;
                        foundGuest = guest;
                        break;
                    }
                }
                if (doesGuestExists) {
                    if (foundGuest[1] >= this.possibleArticles[articleModel]) {
                        foundGuest[1] -= this.possibleArticles[articleModel];
                        foundArticle[2]--;
                        foundGuest[2]++;
                        return `${guestName} successfully purchased the article worth ${this.possibleArticles[articleModel]} points.`;
                    } else {
                        return "You need to more points to purchase the article.";
                    }
                } else {
                    return "This guest is not invited.";
                }


            } else {
                return `The ${articleName} is not available.`;
            }
        } else {
            throw new Error("This article is not found.");
        }

    }

    showGalleryInfo(criteria) {
        if (criteria === 'article') {
            let output = ['Articles information:'];
            for (let article of this.listOfArticles) {
                output.push(`${article[0]} - ${article[1]} - ${article[2]}`);
            }
            return output.join('\n');

        } else if (criteria === 'guest') {
            let output = ['Guests information:'];
            for (let guest of this.guests) {
                output.push(`${guest[0]} - ${guest[2]}`);
            }
            return output.join('\n');
        }
    }
}

// const artGallery = new ArtGallery('Curtis Mayfield');
// console.log(artGallery.addArticle('picture', 'Mona Liza', 3));
// console.log(artGallery.addArticle('Item', 'Ancient vase', 2));
// console.log(artGallery.addArticle('PICTURE', 'Mona Liza', 1));


// const artGallery = new ArtGallery('Curtis Mayfield');
// console.log(artGallery.inviteGuest('John', 'Vip'));
// console.log(artGallery.inviteGuest('Peter', 'Middle'));
// console.log(artGallery.inviteGuest('John', 'Middle'));
// console.log(artGallery.inviteGuest('Ivan', 'Normal'));

// const artGallery = new ArtGallery('Curtis Mayfield');
// artGallery.addArticle('picture', 'Mona Liza', 3);
// artGallery.addArticle('Item', 'Ancient vase', 2);
// artGallery.addArticle('picture', 'Mona Liza', 1);
// artGallery.inviteGuest('John', 'Vip');
// artGallery.inviteGuest('Peter', 'Middle');
// console.log(artGallery.buyArticle('picture', 'Mona Liza', 'John'));
// console.log(artGallery.buyArticle('item', 'Ancient vase', 'Peter'));
// console.log(artGallery.buyArticle('item', 'Mona Liza', 'John'));

const artGallery = new ArtGallery('Curtis Mayfield');
artGallery.addArticle('picture', 'Mona Liza', 3);
artGallery.addArticle('Item', 'Ancient vase', 2);
artGallery.addArticle('picture', 'Mona Liza', 1);
artGallery.inviteGuest('John', 'Vip');
artGallery.inviteGuest('Peter', 'Middle');
artGallery.buyArticle('picture', 'Mona Liza', 'John');
artGallery.buyArticle('item', 'Ancient vase', 'Peter');
console.log(artGallery.showGalleryInfo('article'));
console.log(artGallery.showGalleryInfo('guest'));