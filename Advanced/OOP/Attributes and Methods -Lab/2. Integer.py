from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if type(value) == float:
            return cls(floor(value))
        return "value is not a float"

    @classmethod
    def from_string(cls, value):
        if type(value) == str:
            if value.replace('.', '', 1).isdigit():
                value = float(value)
                return cls(int(value))
        return "wrong type"

    @classmethod
    def from_roman(cls, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in roman:
                num += roman[s[i:i+2]]
                i += 2
            else:
                # print(i)
                num += roman[s[i]]
                i += 1
        return cls(num)

    def add(self, integer):
        # integer: Integer returns  name 'Integer' is not defined, защото хинта е самия клас за който се отнася метода ?
        if isinstance(integer, Integer):
            return self.value + integer.value
        return "number should be an Integer instance"


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))
