class Story {
    constructor(title, creator) {
        this.title = title;
        this.creator = creator;
        this._comments = [];
        this._likes = [];
        this._id = 1;
    }

    get likes() {
        if (this._likes.length === 0) {
            return `${this.title} has 0 likes`;
        }

        if (this._likes.length === 1) {
            return `${this._likes[0]} likes this story!`;
        }

        return `${this._likes[0]} and ${this._likes.length - 1} others like this story!`;
    }

    like(username) {
        if (this._likes.includes(username)) {
            throw new Error("You can't like the same story twice!");
        }

        if (username === this.creator) {
            throw new Error("You can't like your own story!");
        }

        this._likes.push(username);
        return `${username} liked ${this.title}!`;
    }

    dislike(username) {
        const usernameIndex = this._likes.indexOf(username);

        if (usernameIndex > -1) {
            this._likes.splice(usernameIndex, 1);
            return `${username} disliked ${this.title}`;
        }

        throw new Error("You can't dislike this story!");
    }

    comment(username, content, id) {
        const comment = this._comments.find(comment => comment.id === id);
        if (comment) {
            comment.replyID++;
            id = Number(`${comment.id}.${comment.replyID}`);
            comment.replies.push({ id, username, content });
            return "You replied successfully";
        }

        id = this._id;
        this._id++;
        this._comments.push({ id, username, content, replyID: 0, replies: [] });

        return `${username} commented on ${this.title}`;


    }

    toString(criteria) {
        const compareByCriteria = Story.compareTo(criteria);
        
        this._comments.sort(compareByCriteria);
        this._comments.forEach(comment => comment.replies.sort(compareByCriteria));


        let output = [
            `Title: ${this.title}`,
            `Creator: ${this.creator}`,
            `Likes: ${this._likes.length}`,
            `Comments:`
        ];

        for (let comment of this._comments) {
            output.push(`-- ${comment.id}. ${comment.username}: ${comment.content}`);
            for (let reply of comment.replies) {
                output.push(`--- ${reply.id}. ${reply.username}: ${reply.content}`);
            }
        }

        return output.join("\n");
    }

    static compareTo(criteria) {
        return function (a, b) {
            if (criteria === 'asc') {
                return a.id - b.id;
            } else if (criteria === 'desc') {
                return b.id - a.id;
            } else if (criteria === 'username') {
                return a.username.localeCompare(b.username);
            }
        }
    }

}


let art = new Story("My Story", "Anny");
art.like("John");
console.log(art.likes);
art.dislike("John");
console.log(art.likes);
art.comment("Sammy", "Some Content");
console.log(art.comment("Ammy", "New Content"));
art.comment("Zane", "Reply", 1);
art.comment("Jessy", "Nice :)");
console.log(art.comment("SAmmy", "Reply@", 1));
console.log()
console.log(art.toString('username'));
console.log()
art.like("Zane");
console.log(art.toString('desc'));
