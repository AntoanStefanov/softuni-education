function solve(arr) {

    function listProcessor() {
        let list = [];

        return {
            add,
            remove,
            print
        }

        function add(str) {
            list.push(str);
        }
        function remove(str) {
            list = list.filter(x => x !== str);
        }
        function print() {
            console.log(list.join(","));
        }
    }

    let processor = listProcessor();
    for (let data of arr) {
        let [command, str] = data.split(' ');
        if (command === 'add') {
            processor.add(str);
        } else if (command === 'remove') {
            processor.remove(str);
        } else if (command === 'print') {
            processor.print();
        }
    }
}


solve(['add hello', 'add again', 'remove hello', 'add again', 'print']);