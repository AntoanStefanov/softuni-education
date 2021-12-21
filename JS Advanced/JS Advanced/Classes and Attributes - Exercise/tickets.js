function solve(arr, criteria) {
    class Ticket {
        constructor(destination, price, status) {
            this.destination = destination;
            this.price = +price;
            this.status = status;
        }

        static compareTo(a, b) {
            if (criteria === 'price') {
                return a.criteria - b.criteria;
            }
            return a[criteria].localeCompare(b[criteria]);
        }
    }

    let tickets = [];
    for (let t of arr) {
        let [d, p, s] = t.split('|')
        tickets.push(new Ticket(d, p, s))
    }

    tickets.sort(Ticket.compareTo);
    // for (let t of tickets) {
    //     console.log(t);
    // }
    return tickets;
}

solve(['Philadelphia|94.20|available',
    'New York City|95.99|available',
    'New York City|95.99|sold',
    'Boston|126.20|departed'],
    'destination');

solve(['Philadelphia|94.20|available',
    'New York City|95.99|available',
    'New York City|95.99|sold',
    'Boston|126.20|departed'],
    'status');

solve(['Philadelphia|94.20|available',
    'New York City|95.99|available',
    'New York City|95.99|sold',
    'Boston|126.20|departed'],
    'price');