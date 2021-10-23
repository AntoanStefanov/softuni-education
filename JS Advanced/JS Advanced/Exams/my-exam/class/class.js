class SummerCamp {
    constructor(organizer, location) {
        this.organizer = organizer;
        this.location = location;
        this.priceForTheCamp = { "child": 150, "student": 300, "collegian": 500 }
        this.listOfParticipants = [];
    }

    registerParticipant(name, condition, money) {
        if (!(condition in this.priceForTheCamp)) {
            throw new Error("Unsuccessful registration at the camp.");
        }
        let participant = this.listOfParticipants.find(obj => obj.name === name);
        if (participant) {
            return `The ${name} is already registered at the camp.`;
        }

        if (money < this.priceForTheCamp[condition]) {
            return `The money is not enough to pay the stay at the camp.`;
        }

        this.listOfParticipants.push({ name, condition, power: 100, wins: 0 });
        return `The ${name} was successfully registered.`;
    }

    unregisterParticipant(name) {
        let participantIndex = this.listOfParticipants.findIndex(obj => obj.name === name);
        if (participantIndex > -1) {
            this.listOfParticipants.splice(participantIndex, 1);
            return `The ${name} removed successfully.`;
        }

        throw new Error(`The ${name} is not registered in the camp.`);

    }
    timeToPlay(typeOfGame, participant1, participant2) {
        if (typeOfGame === 'WaterBalloonFights') { // za dvama
            let firstParticipant = this.listOfParticipants.find(obj => obj.name === participant1);
            let secondParticipant = this.listOfParticipants.find(obj => obj.name === participant2);

            if (!firstParticipant || !secondParticipant) { // if any name is not present;
                throw new Error(`Invalid entered name/s.`);
            }

            if (firstParticipant.condition !== secondParticipant.condition) {
                throw new Error(`Choose players with equal condition.`);
            }

            if (firstParticipant.power > secondParticipant.power) {
                firstParticipant.wins++;
                return `The ${firstParticipant.name} is winner in the game ${typeOfGame}.`;
            }
            if (secondParticipant.power > firstParticipant.power) {
                secondParticipant.wins++;
                return `The ${secondParticipant.name} is winner in the game ${typeOfGame}.`;
            }

            return `There is no winner.`;


        } else if (typeOfGame === 'Battleship') { // za edin
            let firstParticipant = this.listOfParticipants.find(obj => obj.name === participant1);

            if (!firstParticipant) { // if any name is not present;
                throw new Error(`Invalid entered name/s.`);
            }

            firstParticipant.power += 20;
            return `The ${firstParticipant.name} successfully completed the game ${typeOfGame}.`;
        }
    }

    toString() {
        let output = [`${this.organizer} will take ${this.listOfParticipants.length} participants on camping to ${this.location}`];

        this.listOfParticipants.sort(function (participant1, participant2) {
            return participant2.wins - participant1.wins;
        })

        for (let participant of this.listOfParticipants) {
            output.push(`${participant.name} - ${participant.condition} - ${participant.power} - ${participant.wins}`);
        }

        return output.join('\n');
    }
}


const summerCamp = new SummerCamp("Jane Austen", "Pancharevo Sofia 1137, Bulgaria");
console.log(summerCamp.registerParticipant("Petar Petarson", "student", 300));
console.log(summerCamp.timeToPlay("Battleship", "Petar Petarson"));
console.log(summerCamp.registerParticipant("Sara Dickinson", "child", 200));
// console.log(summerCamp.timeToPlay("WaterBalloonFights", "Petar Petarson", "Sara Dickinson"));
console.log(summerCamp.registerParticipant("Dimitur Kostov", "student", 300));
console.log(summerCamp.timeToPlay("WaterBalloonFights", "Petar Petarson", "Dimitur Kostov"));

console.log(summerCamp.toString());
