function solve(input) {
    let index = 0;
    let data;
    let number;
    let isPrime;
    let primeSum = 0;
    let nonPrimeSum = 0;

    if (false) {
        while (true) {
            data = input[index];
            index++;

            if (data === 'stop') {
                break;
            }
            number = Number(data);

            if (number < 0) {
                console.log('Number is negative.');
                continue;
            }

            isPrime = true;
            for (let i = 2; i < number; i++) {
                if (number % i === 0) {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime) {
                primeSum += number;
            } else {
                nonPrimeSum += number;
            }
        }
    }

    console.log(data);
    console.log(`Sum of all prime numbers is: ${primeSum}`);
    console.log(`Sum of all non prime numbers is: ${nonPrimeSum}`);
}


solve(["3",
    "9",
    "0",
    "7",
    "19",
    "4",
    "stop"])

solve(["30",
    "83",
    "33",
    "-1",
    "20",
    "stop"])