from random import randint, choice
import string


class PolishIDCard:
    def __init__(self):
        self.number = None
        self.letters = {
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15,
            'G': 16,
            'H': 17,
            'I': 18,
            'J': 19,
            'K': 20,
            'L': 21,
            'M': 22,
            'N': 23,
            'O': 24,
            'P': 25,
            'Q': 26,
            'R': 27,
            'S': 28,
            'T': 29,
            'U': 30,
            'V': 31,
            'W': 32,
            'X': 33,
            'Y': 34,
            'Z': 35
        }

    def generate(self):
        doc_letters1 = [choice(list(self.letters.keys())) for i in range(3)]
        doc_letters2 = ([self.letters[i] for i in doc_letters1])
        doc_digits = randint(100000, 999999)
        doc_check = self.check(doc_digits, doc_letters2)
        temp = doc_letters1[0], doc_letters1[1], doc_letters1[2], str(doc_check), str(doc_digits)[1:]
        self.number = ''.join(temp)

        return self.number

    def check(self, doc_digits, doc_letters):
        w1 = [7, 3, 1]
        w2 = [0, 7, 3, 1, 7, 3]

        result1 = sum([x * y for x, y in zip(doc_letters, w1)])

        number = [int(i) for i in str(doc_digits)]
        result2 = sum([x * y for x, y in zip(number, w2)])
        
        result = result1 + result2

        return result % 10

    def get(self):
        return self.number

    def set(self, number):
        self.number = number

    def validate(self, number):
        if len(number) != 9:
            return False
        doc_letters1 = number[0:3]
        doc_letters2 = ([self.letters[i] for i in doc_letters1])
        doc_digits = number[3:10]
        doc_check = int(number[3:4])
        test_check = self.check(doc_digits, doc_letters2)
        if doc_check == test_check:
            return True
        else:
            return False

# test = PolishIDCard()
# test.generate()
# print(test.validate(test.get()))
