function solve(input) {
    let count = 0;
    let words = input[0].split(' ');
    for (let i = 0; i < words.length; i++) {
        count += 1;
    }

    if (count > 10) {
        console.log(`The message is too long to be send! Has ${count} words.`);
    } else {
        console.log('The message was sent successfully!');
    }
}

solve(["This message has exactly eleven words. One more as it's allowed!"]);
