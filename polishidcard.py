from random import randint, choice
import string

class PolishIDCard():
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
        doc_digits = randint(10000, 99999)
        doc_check = self.check(doc_digits, doc_letters2)
        temp = doc_letters1[0], doc_letters1[1], doc_letters1[2], str(doc_check), str(doc_digits)
        self.number = ''.join(temp)

        return(self.number)

    def check(self, doc_digits, doc_letters):
        w1 = [7, 3, 1]
        w2 = [0, 7, 3, 1, 7, 3]

        result1 = sum([x * y for x, y in zip(doc_letters, w1)])

        temp = '0' + str(doc_digits)
        number = [int(i) for i in temp]
        result2 = sum([x * y for x, y in zip(number, w2)])
        
        result = result1 + result2

        return result % 10

    def get(self):
        return self.number
        
    def set(self, number):
        self.number = number

    # todo
    def validate(self, number):
        pass

#test = PolishIDCard()
#print(test.generate())
