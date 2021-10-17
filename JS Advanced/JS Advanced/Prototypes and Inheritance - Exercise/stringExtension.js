(function solve() {
    String.prototype.ensureStart = function (str) {
        let stringValue = this.valueOf();
        if (!this.startsWith(str)) {
            stringValue = str + stringValue;
            return stringValue;
        }
        return stringValue;
    }

    String.prototype.ensureEnd = function (str) {
        let stringValue = this.valueOf();
        if (!this.endsWith(str)) {
            stringValue += str;
            return stringValue;
        }
        return stringValue;
    }

    String.prototype.isEmpty = function () {
        return this.valueOf() === '';
    }

    String.prototype.truncate = function (n) {
        if (n < 4) {
            return ".".repeat(n);
        }
        if (this.toString().length <= n) {
            return this.toString();
        } else {
            let lastIndex = this.toString().substr(0, n - 2).lastIndexOf(" ");
            if (lastIndex != -1) {
                return this.toString().substr(0, lastIndex) + "...";
            } else {
                return this.toString().substr(0, n - 3) + "...";
            }
        }
    };

    String.format = function (string, ...params) {
        for (let index = 0; index < params.length; index++) {
            let param = params[index];
            if (param !== undefined) {
                string = string.replace(`{${index}}`, param);
            }
        }
        return string;
    }

})()



let str = 'my string';
str = str.ensureStart('my');
str = str.ensureStart('hello ');
str = str.truncate(16);
str = str.truncate(14);
str = str.truncate(8);
str = str.truncate(4);
str = str.truncate(2);
str = String.format('The {0} {1} fox',
    'quick', 'brown');
str = String.format('jumps {0} {1}',
    'dog');
